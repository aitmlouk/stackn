# Generated by Django 3.1.6 on 2021-02-20 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0030_auto_20210220_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appinstance',
            name='settings',
        ),
        migrations.AlterField(
            model_name='appinstance',
            name='info',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
