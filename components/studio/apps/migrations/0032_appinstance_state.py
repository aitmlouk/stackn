# Generated by Django 3.1.6 on 2021-02-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0031_auto_20210220_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinstance',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
