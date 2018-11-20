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
from django.shortcuts import redirect, reverse, render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic import UpdateView, ListView, DeleteView, TemplateView, CreateView, FormView

from .api import APIDeleteError, delete_visor, APIClient, import_file


from .forms import EditForm, CategoryForm, PlaceForm, ArchiveForm
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
    pk_url_kwarg = 'file_name'

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        file_name = self.kwargs.get(self.pk_url_kwarg)
        try:
            return queryset.get(img_file__file_name=file_name)
        except ImageData.DoesNotExist:
            pass
        return None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        file_name = self.kwargs.get(self.pk_url_kwarg)
        client = APIClient()
        kwargs['initial'].update(client.get_file(file_name, get_content=True))
        kwargs['initial'].update({'file_name': file_name})
        kwargs.update({'request': self.request})
        return kwargs


class TagView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        client = APIClient()
        res = client.create_tag(request.POST['input'])
        return JsonResponse({'id': res, 'value': res})


class SearchView(LoginRequiredMixin, View):

    template_name = 'administration/search.html'

    def get(self, request, *args, **kwargs):
        if 'file' not in request.GET:
            return HttpResponseRedirect(reverse_lazy('administration:list'))
        filename = request.GET['file']
        client = APIClient()
        data = client.search(filename)
        return render(request, self.template_name, {'search_value': filename, 'list': data})

class Delete(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('administration:list')

    def delete(self, request, *args, **kwargs):
        success_url = self.success_url
        try:
            delete_visor(self.kwargs['file_name'])
        except APIDeleteError as e:
            return JsonResponse({'error': str(e)})

        return JsonResponse({'url': success_url})


class TaxonomyView(LoginRequiredMixin, TemplateView):
    template_name = 'administration/taxonomy.html'

    def get_context_data(self, **kwargs):
        ctx = super(TaxonomyView, self).get_context_data(**kwargs)
        ctx.update({
            'category_form': CategoryForm(),
            'place_form': PlaceForm(),
            'archive_form': ArchiveForm(),
            'msg': self.request.session.pop('msg', None)
        })
        return ctx


class AddCategoryView(LoginRequiredMixin, CreateView):

    def get(self, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('administration:taxonomies'))

    def post(self, request, *args, **kwargs):
        form = CategoryForm(data=request.POST, request=request)
        if form.is_valid():
            result = form.save()
            if result:
                self.request.session['msg'] = 'La categoria {} e\' stata aggiunta'.format(result['Name'])
            return HttpResponseRedirect(reverse_lazy('administration:taxonomies'))
        else:
            return render(request, 'administration/taxonomy.html', {
                'category_form': form, 'msg': request.session.pop('msg', None)
            })


class AddPlaceView(LoginRequiredMixin, CreateView):

    def get(self, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('administration:taxonomies'))

    def post(self, request, *args, **kwargs):
        form = PlaceForm(data=request.POST, request=request)
        if form.is_valid():
            result = form.save()
            if result:
                self.request.session['msg'] = 'Location {} e\' stata aggiunta'.format(result['Nome'])
            return HttpResponseRedirect(reverse_lazy('administration:taxonomies'))
        else:
            return render(request, 'administration/taxonomy.html', {
                'place_form': form, 'msg': request.session.pop('msg', None)
            })


class AddArchiveView(LoginRequiredMixin, CreateView):

    def get(self, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('administration:taxonomies'))

    def post(self, request, *args, **kwargs):
        form = ArchiveForm(data=request.POST, request=request)
        if form.is_valid():
            result = form.save()
            if result:
                self.request.session['msg'] = 'L\'archivio {} e\' stato aggiunto'.format(result)
            return HttpResponseRedirect(reverse_lazy('administration:taxonomies'))
        else:
            return render(request, 'administration/taxonomy.html', {
                'archive_form': form, 'msg': request.session.pop('msg', None)
            })
