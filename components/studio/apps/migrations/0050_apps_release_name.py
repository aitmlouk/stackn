# Generated by Django 3.1.7 on 2021-04-09 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_auto_20210409_1314'),
        ('apps', '0049_auto_20210318_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='apps',
            name='release_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.releasename'),
        ),
    ]
