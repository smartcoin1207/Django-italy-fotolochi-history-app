# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpRequest
from .forms import EditForm
from .models import ImageData, ImageFile
from django.views import View
from django.views.generic import UpdateView, ListView
from os import listdir
from os.path import isfile, join
from .helpers import *
import json
import random
import string
import os
from django.views.decorators.csrf import csrf_exempt



def hash_file_name(filename):
    key = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(30))
    filename = key + '.' + filename.split('.')[1]
    return filename


class Login(auth_views.LoginView):
    template_name = 'administration/login.html'

#
#     def post(self, request, *args, **kwargs):
#         data = {'username': request.POST.get('username'), 'password': request.POST.get('password')}
#         form = LoginForm(data=data)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('administration:list'))
#             else:
#                 return render(request, 'administration/login.html', {'form': form, 'errors': 'username or pasword incorrect'})
#         else:
#             return render(request, 'administration/login.html', {'form': LoginForm()})
#
#     def get(self, request, *args, **kwargs):
#         if request.user and request.user.is_authenticated:
#             return HttpResponseRedirect(reverse('administration:list'))
#         else:
#             return render(request, 'administration/login.html', {'form': LoginForm()})
#
#
class Logout(auth_views.LogoutView):
    template_name = 'administration/login.html'
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return HttpResponseRedirect(reverse('administration:login'))



class List(LoginRequiredMixin, ListView):

    model = ImageData
    template_name = 'administration/list.html'
    context_object_name = 'list'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(List, self).get_context_data(object_list=object_list, **kwargs)
        ctx['msg'] = self.request.session.pop('msg', '')
        return ctx


class GetNew(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        from fotolochi import settings

        dir = settings.MEDIA_ROOT
        original_tmp_dir = dir + 'original_tmp/'
        original_dir = dir + 'original/'
        thumb_dir = dir + 'thumb/'
        preview_dir = dir + 'preview/'
        files = [f for f in listdir(original_tmp_dir) if isfile(join(original_tmp_dir, f))]
        # And what to do if the same file was uploaded under another name?
        files_in_db = ImageFile.objects.filter(file_name__in=files).values_list('file_name', flat=True)
        if files:
            # TODO: move to Celery tasks
            for file in files:
                if file not in files_in_db:

                    orientation = check_orientation(original_tmp_dir + file)
                    color = detect_color_image(file=original_tmp_dir + file)
                    thumb_name = 'thumb_' + file
                    preview_name = 'prev_' + file

                    original = Image.open(original_tmp_dir + file)
                    ext_original = hash_file_name(file)
                    original.save(original_dir + ext_original)

                    ext_thumb = hash_file_name(thumb_name)
                    thumb = resize_and_crop(original_tmp_dir + file, thumb_dir + ext_thumb, size=(128, 128))

                    ext_prev = hash_file_name(preview_name)
                    preview = make_preview(original_tmp_dir + file, preview_dir + ext_prev, size=(1000, 1000))

                    if not preview:
                        preview_name = 'None'
                    if not thumb:
                        thumb_name = 'None'

                    img = ImageFile(file_name=file,
                                    original_name='original/' + ext_original,
                                    thumb_name='thumb/' + ext_thumb,
                                    preview_name='preview/' + ext_prev,
                                    is_new=True,
                                    is_color=color,
                                    orientation=orientation)

                    img.save()
                    img_data = ImageData(img_file=img)
                    img_data.save()

                    os.remove(original_tmp_dir + file)
                    request.session['msg'] = 'New files was added to list'
        else:
            request.session['msg'] = 'New files in the original_tmp directory not found'

        return HttpResponseRedirect(reverse('administration:list'))


class Edit(LoginRequiredMixin, UpdateView):

    template_name = 'administration/edit.html'
    form_class = EditForm
    queryset = ImageData.objects.select_related('img_file').all()
    success_url = reverse_lazy('administration:list')

    # def get(self, request, data_id, *args, **kwargs):
    #     image_data = ImageData.objects.get(id=data_id) if int(data_id) else None
    #     form = EditForm(instance=image_data, use_required_attribute=False)
    #     return render(request, 'administration/edit.html', {'data_id': int(data_id), 'form': form})
    #
    # @csrf_exempt
    # def post(self, request, data_id, *args, **kwargs):
    #     image_data = ImageData.objects.get(id=data_id)
    #     data = {}
    #     for i in json.loads(request.body.decode('utf-8')):
    #         data.update({i['name']: i['value']})
    #
    #     form = EditForm(instance=image_data, data=data, use_required_attribute=False)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('administration:list'))
    #     else:
    #         return render(request, 'administration/edit.html', {'form': form,
    #                                                     'data_id': int(data_id),
    #                                                     'errors': dict(form.errors.items())})
