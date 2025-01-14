# Generated by Django 3.1.6 on 2021-03-18 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0049_auto_20210318_1401'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0018_auto_20210308_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='MLFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('mlflow_url', models.CharField(max_length=512)),
                ('s3_host', models.CharField(max_length=512)),
                ('access_key', models.CharField(max_length=512)),
                ('secret_key', models.CharField(max_length=512)),
                ('region', models.CharField(blank=True, default='', max_length=512)),
                ('ba_username', models.CharField(blank=True, default='', max_length=100)),
                ('ba_password', models.CharField(blank=True, default='', max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('app', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mlflowobj', to='apps.appinstance')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mlflow_project', to='projects.project')),
            ],
        ),
    ]
