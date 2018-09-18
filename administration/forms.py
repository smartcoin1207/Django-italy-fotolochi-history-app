from django import forms

from .models import ImageData, ImageFile
from .helpers import COLOR_CHOICES, ORIENTATION_CHOICES, SUPPORT_CHOICES
from api.core import APIClient, APIUpdateError, APICategoryError, APITagError, APIPlaceError


class EditForm(forms.ModelForm):

    preview = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), label="Preview", required=False, max_length=128
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Titolo'}), label="Title", required=False, max_length=128)

    short_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'textarea', 'placeholder': 'Descrizione breve'}), label="Short Description", required=False, max_length=128)

    full_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'textarea', 'placeholder': 'Descrizione'}), label="Full Description", required=False, max_length=256)

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
        widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'aaaa'}), label="Year", required=False
    )

    is_decennary = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'}), label="Decade", required=False
    )

    support = forms.ChoiceField(
        widget=forms.Select(), label="Archivio", required=False, choices=SUPPORT_CHOICES
    )

    rating = forms.IntegerField(
        widget=forms.Select(choices=[(i,i) for i in range(1,6)]), label="Rating", required=False
    )

    creative = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'}), label="Creative", required=False
    )

    is_publish = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'}), label="Is Publish", required=False
    )

    place = forms.ChoiceField(
        widget=forms.Select(attrs={}), label="Place", required=False
    )

    categories = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={}), label="Categorie", required=False
    )

    tags = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={}), label="Tags", required=False
    )

    archive = forms.ChoiceField(
        widget=forms.Select(), label="Archivio", required=False
    )

    scope = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'radio'}), choices=ImageData.SCOPE, label="Utenza", required=False
    )

    color = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'radio'}), choices=COLOR_CHOICES, label='Colore', required=False
    )

    orientation = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'radio'}), choices=ORIENTATION_CHOICES, label='Orientation', required=False
    )

    class Meta:
        model = ImageData
        exclude = []
        fields = ['preview', 'title', 'short_description', 'full_description', 'rating', 'creative', 'is_publish',
                  'place', 'tags', 'categories', 'archive', 'notes', 'day', 'month', 'year', 'is_decennary',
                  'scope', 'orientation', 'color', 'support']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EditForm, self).__init__(*args, **kwargs)
        self.client = APIClient()
        if self.instance is not None:
            self.img_file = self.instance.img_file
            self.fields['preview'].initial = self.instance.img_file.preview_name
            self.fields['place'].choices = [['', 'Select place']] + self.client.places
            self.fields['tags'].choices = [['', 'Select tag']] + [(i, i) for i in self.client.tags]
            self.fields['categories'].choices = [['', 'Select category']] + self.client.categories
            self.fields['archive'].choices = [['', 'Select archive']] + self.client.archives
            self.fields['color'].initial = self.instance.img_file.color
            self.fields['orientation'].initial = self.instance.img_file.orientation

    def clean(self):
        super(EditForm, self).clean()
        self.cleaned_data['status'] = ImageData.PRODUCT_STATUS_PUBLISHED \
            if self.cleaned_data['is_publish'] else ImageData.PRODUCT_STATUS_NOT_PUBLISHED

    def save(self, commit=True):
        update_connections = False
        self.cleaned_data.update({
            'file_name': self.img_file.file_name
        })
        try:
            if self.instance.api_id:
                update_connections = True
            resp = self.client.update_visor(self.instance.api_id, **self.cleaned_data)
            if update_connections:
                tags_to_delete = set(self.initial['tags']) - set(self.cleaned_data['tags'])
                tags_to_add = set(self.cleaned_data['tags']) - set(self.initial['tags'])

                for tag in tags_to_add:
                    self.client.add_tag_to_visor(self.instance.api_id, tag)

                for tag in tags_to_delete:
                    self.client.delete_tag_from_visor(self.instance.api_id, tag)

                categories_to_delete = set(self.initial['categories']) - set(self.cleaned_data['categories'])
                categories_to_add = set(self.cleaned_data['categories']) - set(self.initial['categories'])

                for category in categories_to_add:
                    self.client.add_category_to_visor(self.instance.api_id, category)

                for category in categories_to_delete:
                    self.client.delete_category_from_visor(self.instance.api_id, category)

                # TODO: Place - make many places

        except (APIUpdateError, APICategoryError, APITagError, APIPlaceError) as e:
            self.request.session['msg'] = str(e)
        else:
            super(EditForm, self).save(commit=commit)
            self.instance.api_id = resp['_key']
            self.instance.save()
        self.instance.img_file.color = self.cleaned_data['color']
        self.instance.img_file.orientation = self.cleaned_data['orientation']
        self.instance.img_file.save()
        self.instance.mark_as_completed()

        return self.instance
