# Generated by Django 2.1 on 2018-11-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0015_auto_20181019_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedata',
            name='full_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='imagedata',
            name='short_description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='imagedata',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
