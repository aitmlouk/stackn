# Generated by Django 3.1.6 on 2021-03-01 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_environment_appenv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flavor',
            name='cpu',
        ),
        migrations.RemoveField(
            model_name='flavor',
            name='gpu',
        ),
        migrations.RemoveField(
            model_name='flavor',
            name='mem',
        ),
        migrations.AddField(
            model_name='flavor',
            name='cpu_lim',
            field=models.TextField(blank=True, default='1000m', null=True),
        ),
        migrations.AddField(
            model_name='flavor',
            name='cpu_req',
            field=models.TextField(blank=True, default='200m', null=True),
        ),
        migrations.AddField(
            model_name='flavor',
            name='ephmem_lim',
            field=models.TextField(blank=True, default='200Mi', null=True),
        ),
        migrations.AddField(
            model_name='flavor',
            name='ephmem_req',
            field=models.TextField(blank=True, default='200Mi', null=True),
        ),
        migrations.AddField(
            model_name='flavor',
            name='gpu_lim',
            field=models.TextField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='flavor',
            name='gpu_req',
            field=models.TextField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='flavor',
            name='mem_lim',
            field=models.TextField(blank=True, default='3Gi', null=True),
        ),
        migrations.AddField(
            model_name='flavor',
            name='mem_req',
            field=models.TextField(blank=True, default='0.5Gi', null=True),
        ),
        migrations.AddField(
            model_name='flavor',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]
