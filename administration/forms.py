from django import forms
from datetime import datetime

from .models import ImageData, Place, Tag, Category, ImageFile
from api.core import APIClient

# class LoginForm(forms.Form):
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}), label="Username", required=True, max_length=50)
#
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Password", required=True, max_length=50)
#
#     def __init__(self, *args, **kwargs):
#         super(LoginForm, self).__init__(*args, **kwargs)


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

    rating = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}), label="Rating", required=False
    )

    creative = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'pure-checkbox'}), label="Creative", required=False
    )

    is_publish = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'pure-checkbox'}), label="Is Publish", required=False
    )

    places = forms.ChoiceField(
        widget=forms.Select(), label="Places", required=False
    )

    categories = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={}), label="Categorie", required=False
    )

    tags = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={}), label="Tags", required=False
    )

    class Meta:
        model = ImageData
        exclude = []
        fields = ['preview', 'title', 'short_description', 'full_description', 'rating', 'creative', 'is_publish',
                  'places']

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.client = APIClient()
        if self.instance.id is not None:
            self.img_file = self.instance.img_file
            self.fields['preview'].initial = self.instance.img_file.preview_name
            self.fields['places'].choices = [['', 'Select place']] + self.client.places
            self.fields['tags'].choices = [['', 'Select tag']] + [(i, i) for i in self.client.tags]
            self.fields['categories'].choices = [['', 'Select tag']] + self.client.categories
            # self.fields['group'].initial = [(i.group.id, i.group.name) for i in SchoolToUserToGroup.objects.filter(user_id=self.instance.id).all()]

    def clean(self):
        cleaned_data = super(EditForm, self).clean()

    def save(self):
        instance = super(EditForm, self).save()
        instance.date_updated = datetime.now()
        instance.save()
        return instance
