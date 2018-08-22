from django import forms

from .models import ImageData
from api.core import APIClient


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

    decennary_year = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'aaaa'}), label="Year", required=False
    )

    is_decennary = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'}), label="Decade", required=False
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
        widget=forms.Select(), label="Place", required=False
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

    status = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'radio'}), choices=ImageData.PRODUCT_STATUS, label="Stato Prodotto", required=False
    )

    scope = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'radio'}), choices=ImageData.SCOPE, label="Utenza", required=False
    )

    class Meta:
        model = ImageData
        exclude = []
        fields = ['preview', 'title', 'short_description', 'full_description', 'rating', 'creative', 'is_publish',
                  'place', 'tags', 'categories', 'archive']

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.client = APIClient()
        if self.instance is not None:
            self.img_file = self.instance.img_file
            self.fields['preview'].initial = self.instance.img_file.preview_name
            self.fields['place'].choices = [['', 'Select place']] + self.client.places
            self.fields['tags'].choices = [['', 'Select tag']] + [(i, i) for i in self.client.tags]
            self.fields['categories'].choices = [['', 'Select tag']] + self.client.categories
            self.fields['archive'].choices = [['', 'Select archive']] + self.client.archives

    def save(self, commit=True):
        instance = super(EditForm, self).save(commit=commit)
        self.cleaned_data.update({
            'file_name': self.img_file.file_name
        })
        resp = self.client.update_visor(instance.api_id, **self.cleaned_data)
        import pudb;pudb.set_trace()
        instance.api_id = resp['_key']
        instance.save()
        return instance