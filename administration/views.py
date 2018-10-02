# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string
import os
from os import listdir
from os.path import isfile, join

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic import UpdateView, ListView, DeleteView

from .api import APIDeleteError, delete_image_data, APIClient

from .helpers import *
from .forms import EditForm
from .models import ImageData, ImageFile


def hash_file_name(filename):
    key = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(30))
    filename = key + '.' + filename.split('.')[1]
    return filename


class Login(auth_views.LoginView):
    template_name = 'administration/login.html'


class Logout(auth_views.LogoutView):
    template_name = 'administration/login.html'


class List(LoginRequiredMixin, ListView):

    model = ImageData
    template_name = 'administration/list.html'
    context_object_name = 'list'
    ordering = ('-date_updated')
    paginate_by = 5
    queryset = ImageData.objects.filter(is_completed=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(List, self).get_context_data(object_list=object_list, **kwargs)
        ctx['msg'] = self.request.session.pop('msg', '')
        return ctx


class GetNew(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        client = APIClient()
        dir = settings.MEDIA_ROOT
        original_tmp_dir = settings.FTP_ROOT
        original_dir = dir + 'original/'
        thumb_dir = dir + 'thumb/'
        preview_dir = dir + 'preview/'
        files = [f for f in listdir(original_tmp_dir) if isfile(join(original_tmp_dir, f))]

        files_in_db = list(ImageFile.objects.filter(file_name__in=files).values_list('file_name', flat=True))
        if files:
            # TODO: move to Celery tasks
            for file in files:
                file_name = os.path.basename(file)
                file_info = client.get_file(file_name)
                if not file_info and file_name not in files_in_db:

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
                                    color=color,
                                    orientation=orientation)

                    img.save()
                    img_data = ImageData(img_file=img)
                    img_data.save()
                    # XXX: DO NOT UNCOMMENT!!!! FILES SHOULD NOT BE DELETED!
                    # os.remove(original_tmp_dir + file)
                    request.session['msg'] = 'New files was added to list'
                else:
                    request.session['msg'] = 'New files in the original_tmp directory not found'
        else:
            request.session['msg'] = 'New files in the original_tmp directory not found'

        return HttpResponseRedirect(reverse('administration:list'))


class Edit(LoginRequiredMixin, UpdateView):

    template_name = 'administration/edit.html'
    form_class = EditForm
    queryset = ImageData.objects.select_related('img_file').all()
    success_url = reverse_lazy('administration:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class Delete(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('administration:list')
    queryset = ImageData.objects.select_related('img_file').all()

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            delete_image_data(self.object)
        except APIDeleteError as e:
            return JsonResponse({'error': str(e)})

        return HttpResponseRedirect(success_url)
