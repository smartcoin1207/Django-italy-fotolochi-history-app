# Generated by Django 2.1 on 2018-10-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0014_auto_20180921_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedata',
            name='is_publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='imagedata',
            name='support',
            field=models.CharField(blank=True, choices=[(None, 'Senza supporto'), ('6x6', '6x6'), ('35mm', '35mm'), ('6x9', '6x9')], max_length=255, null=True),
        ),
    ]
