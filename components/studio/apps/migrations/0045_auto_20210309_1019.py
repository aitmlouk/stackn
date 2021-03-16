# Generated by Django 3.1.6 on 2021-03-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0044_apps_name_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appinstance',
            name='name_field',
        ),
        migrations.RemoveField(
            model_name='apps',
            name='name_field',
        ),
        migrations.AlterField(
            model_name='appinstance',
            name='table_field',
            field=models.TextField(blank=True, null=True),
        ),
    ]
