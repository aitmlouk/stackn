# Generated by Django 3.1.6 on 2021-02-19 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0026_remove_appinstance_vol_dependencies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appinstance',
            name='helmchart',
        ),
    ]
