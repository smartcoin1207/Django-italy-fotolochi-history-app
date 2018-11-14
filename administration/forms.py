from datetime import datetime

from django import forms

from .models import ImageData, ImageFile
from .helpers import COLOR_CHOICES, ORIENTATION_CHOICES, SUPPORT_CHOICES
from api.core import APIClient, APIUpdateError, APICategoryError, APITagError, APIPlaceError


class CategoryForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nome'}))
    parent = forms.ChoiceField(widget=forms.Select(attrs={'id': 'id_categories'}), required=False)

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.client = APIClient()
        self.fields['parent'].choices = [['', 'Root category']] + self.client.categories

    def save(self):
        res = self.client.create_category(self.cleaned_data['parent'] or '0', self.cleaned_data['name'])
        return res


class PlaceForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nome'}))
    parent = forms.ChoiceField(widget=forms.Select(attrs={'id': 'id_place'}), required=False)

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.client = APIClient()
        self.fields['parent'].choices = [['', 'Root place']] + self.client.places

    def save(self):
        res = self.client.create_place(self.cleaned_data['name'])
        return res


class ArchiveForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nome'}))

    def __init__(self, *args, **kwargs):
        super(ArchiveForm, self).__init__(*args, **kwargs)
        self.client = APIClient()

    def save(self):
        res = self.client.create_archive(self.cleaned_data['name'])
        return res



class EditForm(forms.ModelForm):

    # preview = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}, ), label="Preview", required=True, max_length=128
    # )

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Titolo'}), label="Title", required=True, max_length=128)

    short_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'textarea', 'placeholder': 'Descrizione breve'}), label="Short Description", required=True, max_length=128)

    full_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'textarea', 'placeholder': 'Descrizione'}), label="Full Description", required=True, max_length=256)

    notes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'textarea', 'placeholder': 'Note'}),
        label="Note", required=False, max_length=256)

    day = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'dd'}), label="Day", required=False
    )
    month = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'mm'}), label="Month", required=False
    )

    year = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'aaaa'}), label="Year", required=True
    )

    is_decennary = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'}), label="Decade", required=False
    )

    support = forms.ChoiceField(
        widget=forms.Select(), label="Archivio", required=False, choices=SUPPORT_CHOICES
    )

    rating = forms.IntegerField(
        widget=forms.Select(choices=[(i,i) for i in range(1,6)]), label="Rating", required=True
    )

    creative = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'}), label="Creative", required=False
    )

    is_publish = forms.BooleanField(
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'}), label="Is Publish", required=False
    )

    place = forms.ChoiceField(
        widget=forms.Select(attrs={}), label="Place", required=True
    )

    categories = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={}), label="Categorie", required=True
    )

    tags = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={}), label="Tags", required=True
    )

    archive = forms.ChoiceField(
        widget=forms.Select(), label="Archivio", required=True
    )

    scope = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'radio'}), choices=ImageData.SCOPE, label="Utenza", required=False
    )

    color = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'radio'}), choices=COLOR_CHOICES, label='Colore', required=True
    )

    orientation = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'radio'}), choices=ORIENTATION_CHOICES, label='Orientation',
        required=True
    )

    class Meta:
        model = ImageData
        exclude = []
        fields = ['title', 'short_description', 'full_description', 'rating', 'creative', 'is_publish',
                  'place', 'tags', 'categories', 'archive', 'notes', 'day', 'month', 'year', 'is_decennary',
                  'scope', 'orientation', 'color', 'support']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EditForm, self).__init__(*args, **kwargs)
        self.client = APIClient()
        if self.instance is not None and getattr(self.instance, 'img_file', False):
            self.img_file = self.instance.img_file
            self.fields['color'].initial = self.instance.img_file.color
            self.fields['orientation'].initial = self.instance.img_file.orientation
        self.fields['place'].choices = [['', 'Select place']] + self.client.places
        self.fields['tags'].choices = [['', 'Select tag']] + [(i, i) for i in self.client.tags]
        self.fields['categories'].choices = [['', 'Select category']] + self.client.categories
        self.fields['archive'].choices = self.client.archives

    def clean_year(self):
        value = self.cleaned_data.get('year')
        if value > datetime.now().year:
            raise forms.ValidationError('Year should be less or equal current year')
        if value < 0:
            raise forms.ValidationError('Can\'t assign negative values to year')
        return value

    def clean(self):
        super(EditForm, self).clean()
        self.cleaned_data['status'] = ImageData.PRODUCT_STATUS_PUBLISHED \
            if self.cleaned_data['is_publish'] else ImageData.PRODUCT_STATUS_NOT_PUBLISHED
        if self.cleaned_data.get('month') and not self.cleaned_data.get('day'):
            self.add_error('day', 'Please define day')
        if self.cleaned_data.get('day') and not self.cleaned_data.get('month'):
            self.add_error('month', 'Please define month')
        if self.cleaned_data.get('is_decennary') and (self.cleaned_data.get('day') or self.cleaned_data.get('month')):
            self.add_error('is_decennary', 'Remove day/month values if it is decennary')

    def save(self, commit=True):
        # update_connections = False
        self.cleaned_data.update({
            'file_name': self.img_file.file_name if getattr(self, 'img_file', False) else self.initial['file_name']
        })
        try:
            # if self.instance.api_id:
            #     update_connections = True
            resp = self.client.update_visor(self.instance.api_id, **self.cleaned_data)
            # if update_connections:
            #     tags_to_delete = set(self.initial['tags']) - set(self.cleaned_data['tags'])
            #     tags_to_add = set(self.cleaned_data['tags']) - set(self.initial['tags'])
            #
            #     for tag in tags_to_add:
            #         self.client.add_tag_to_visor(self.instance.api_id, tag)
            #
            #     for tag in tags_to_delete:
            #         self.client.delete_tag_from_visor(self.instance.api_id, tag)
            #
            #     categories_to_delete = set(self.initial['categories']) - set(self.cleaned_data['categories'])
            #     categories_to_add = set(self.cleaned_data['categories']) - set(self.initial['categories'])
            #
            #     for category in categories_to_add:
            #         self.client.add_category_to_visor(self.instance.api_id, category)
            #
            #     for category in categories_to_delete:
            #         self.client.delete_category_from_visor(self.instance.api_id, category)

        except (APIUpdateError, APICategoryError, APITagError, APIPlaceError) as e:
            self.request.session['msg'] = str(e)
        else:
            if getattr(self, 'img_file', False):
                super(EditForm, self).save(commit=commit)
                self.instance.api_id = resp['_key']
                self.instance.save()
        if getattr(self, 'img_file', False):
            self.instance.img_file.color = self.cleaned_data['color']
            self.instance.img_file.orientation = self.cleaned_data['orientation']
            self.instance.img_file.save()
            self.instance.mark_as_completed()

        return self.instance
