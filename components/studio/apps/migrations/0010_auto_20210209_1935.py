# Generated by Django 2.2.13 on 2021-02-09 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_apps_exposed'),
    ]

    operations = [
        migrations.AddField(
            model_name='apps',
            name='port',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='apps',
            name='schema',
            field=models.CharField(default='https://', max_length=10),
        ),
    ]
