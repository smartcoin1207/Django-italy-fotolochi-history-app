from django.db import models


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
    is_color = models.BooleanField(default=True)
    orientation = models.CharField(null=True, max_length=128)
    is_new = models.BooleanField(default=True)

    class Meta:
        db_table = 'image_file'


class ImageData(models.Model):
    img_file = models.ForeignKey(ImageFile, on_delete=models.CASCADE)
    api_id = models.CharField(max_length=255, unique=True, db_index=True, null=True, blank=True)
    title = models.CharField(null=True, max_length=128)
    short_description = models.CharField(null=True, max_length=128)
    full_description = models.CharField(null=True, max_length=128)
    date_updated = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(null=True)
    creative = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    categories = models.ManyToManyField(Category, null=True, blank=True)
    place = models.ForeignKey(Place, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'image_data'