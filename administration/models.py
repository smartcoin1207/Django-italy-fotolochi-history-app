from separatedvaluesfield.models import SeparatedValuesField

from django.db import models

from .helpers import ORIENTATION_CHOICES, COLOR_CHOICES, SUPPORT_CHOICES


class Place(models.Model):
    name = models.CharField(null=True, max_length=128)

    class Meta:
        db_table = 'places'


class Category(models.Model):
    name = models.CharField(null=True, max_length=128)

    class Meta:
        db_table = 'categories'


class Tag(models.Model):
    name = models.CharField(null=True, max_length=128)
    weight = models.IntegerField(default=1)

    class Meta:
        db_table = 'tags'


class ImageFile(models.Model):

    file_name = models.CharField(null=True, max_length=128, db_index=True)
    original_name = models.CharField(null=True, max_length=128)
    thumb_name = models.CharField(null=True, max_length=128)
    preview_name = models.CharField(null=True, max_length=128)
    added_date = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=10, null=True, blank=True, choices=COLOR_CHOICES)
    orientation = models.IntegerField(null=True, blank=True, choices=ORIENTATION_CHOICES)
    is_new = models.BooleanField(default=True)

    class Meta:
        db_table = 'image_file'


class ImageData(models.Model):
    PRODUCT_STATUS_PUBLISHED = 'S'
    PRODUCT_STATUS_NOT_PUBLISHED= 'N'
    PRODUCT_STATUS = (
        (PRODUCT_STATUS_PUBLISHED, 'Publicato'),
        (PRODUCT_STATUS_NOT_PUBLISHED, 'Non publicato')
    )

    ONLY_EDITORIAL = 'S'
    EDITORIAL_AND_STAMP = 'N'
    SCOPE = (
        (ONLY_EDITORIAL, 'Solo editoriale'),
        (EDITORIAL_AND_STAMP, 'Editoriale e stampa')
    )

    img_file = models.ForeignKey(ImageFile, on_delete=models.CASCADE)
    api_id = models.CharField(max_length=255, unique=True, db_index=True, null=True, blank=True)
    title = models.CharField(null=True, max_length=128)
    short_description = models.CharField(null=True, max_length=128)
    full_description = models.CharField(null=True, max_length=128)
    date_updated = models.DateTimeField(auto_now=True)
    day = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    is_decennary = models.BooleanField(default=False)
    rating = models.IntegerField(null=True)
    creative = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)
    tags = SeparatedValuesField(max_length=255, null=True, blank=True)
    categories = SeparatedValuesField(max_length=255, null=True, blank=True, token=';')
    place = models.TextField(null=True, blank=True)
    archive = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=PRODUCT_STATUS, default=PRODUCT_STATUS_NOT_PUBLISHED)
    scope = models.CharField(max_length=1, choices=SCOPE, default=ONLY_EDITORIAL)
    support = models.CharField(max_length=255, null=True, blank=True, choices=SUPPORT_CHOICES)
    is_completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'image_data'

    def mark_as_completed(self):
        if self.api_id and self.place and self.archive and self.title and \
                self.short_description and self.full_description and \
                self.categories and len(self.categories) > 0 and \
                self.tags and len(self.tags) and self.rating and \
                self.year:
            self.is_completed = True
            self.save()
