# Generated by Django 2.2.13 on 2021-02-17 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0022_auto_20210216_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appinstance',
            name='permission',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apps.AppPermission'),
        ),
    ]