# Generated by Django 3.1.6 on 2021-03-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_auto_20210313_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='objecttype',
            name='slug',
            field=models.CharField(blank=True, default='model', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='objecttype',
            name='name',
            field=models.CharField(blank=True, default='Model', max_length=100, null=True),
        ),
    ]
