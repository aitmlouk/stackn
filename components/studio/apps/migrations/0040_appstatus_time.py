# Generated by Django 3.1.6 on 2021-02-22 22:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0039_remove_appstatus_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appstatus',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
