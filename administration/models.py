from django.db import models

# Create your models here.


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
    title = models.CharField(null=True, max_length=128)
    short_description = models.CharField(null=True, max_length=128)
    full_description = models.CharField(null=True, max_length=128)
    date_updated = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(null=True)
    creative = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)

    class Meta:
        db_table = 'image_data'


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


class ImageToPlace(models.Model):
    image = models.ForeignKey(ImageFile, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images_to_ places'


class ImageToCategory(models.Model):
    image = models.ForeignKey(ImageFile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images_to_ categories'


class ImageToTag(models.Model):
    image = models.ForeignKey(ImageFile, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images_to_ tags'
