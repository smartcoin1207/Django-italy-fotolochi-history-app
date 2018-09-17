# Generated by Django 2.1 on 2018-09-11 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0009_auto_20180823_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagedata',
            name='support',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='color',
            field=models.CharField(blank=True, choices=[('B/N', 'B/N'), ('C', 'Color')], max_length=10, null=True),
        ),
    ]