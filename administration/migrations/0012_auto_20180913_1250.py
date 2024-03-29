# Generated by Django 2.1 on 2018-09-13 12:50

from django.db import migrations, models
from ..helpers import COLORS

def update_color(apps, schema_editor):
    ImageFile = apps.get_model('administration', 'ImageFile')

    for image in ImageFile.objects.all():
        if image.color not in COLORS:
            image.color = 'COL'
        image.save()


def reverse_color(apps, schema_editor):
    ImageFile = apps.get_model('administration', 'ImageFile')

    for image in ImageFile.objects.all():
        if image.color == 'COL':
            image.color = 'C'
        image.save()


def update_categories_token(apps, schema_editor):
    ImageData = apps.get_model('administration', 'ImageData')

    for image in ImageData.objects.all():
        if image.categories:
            image.categories = ';'.join(image.categories)
            image.save()


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0011_remove_imagedata_decennary_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedata',
            name='support',
            field=models.CharField(blank=True, choices=[('6x6', '6x6'), ('35mm', '35mm'), ('6x9', '6x9')],
                                   max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='color',
            field=models.CharField(blank=True, choices=[('B/N', 'B/N'), ('COL', 'Color')], max_length=10, null=True),
        ),
        migrations.RunPython(update_color, reverse_color),
        migrations.RunPython(update_categories_token, lambda x,y: None)
    ]
