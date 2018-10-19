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

from .api import APIDeleteError, delete_image_data, APIClient, import_file


from .forms import EditForm
from .models import ImageData, ImageFile


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
        files = [f for f in listdir(settings.FTP_ROOT) if isfile(join(settings.FTP_ROOT, f)) and f.lower().endswith('jpg')]
        files_in_db = list(ImageFile.objects.filter(file_name__in=files).values_list('file_name', flat=True))
        if files:
            # TODO: move to Celery tasks
            for file in files:
                file_path = os.path.join(settings.FTP_ROOT, file)
                file_name = os.path.basename(file)
                file_info = client.get_file(file_name)
                if file_name not in files_in_db:
                    import_file(file_path, file_name, file_info=file_info)
                    request.session['msg'] = 'New files was added to list'
                else:
                    request.session['msg'] = 'New files in the original_tmp directory not found'
                os.remove(file_path)
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


class TagView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        client = APIClient()
        res = client.create_tag(request.POST['input'])
        return JsonResponse({'id': res, 'value': res})

# class Delete(LoginRequiredMixin, DeleteView):
#     success_url = reverse_lazy('administration:list')
#     queryset = ImageData.objects.select_related('img_file').all()
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         try:
#             delete_image_data(self.object)
#         except APIDeleteError as e:
#             return JsonResponse({'error': str(e)})
#
#         return HttpResponseRedirect(success_url)
