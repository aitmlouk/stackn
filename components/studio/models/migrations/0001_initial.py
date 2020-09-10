# Generated by Django 2.2.13 on 2020-08-31 08:56

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=255)),
                ('release_type', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('access', models.CharField(choices=[('PR', 'Private'), ('LI', 'Limited'), ('PU', 'Public')], default='PR', max_length=2)),
                ('resource', models.URLField(blank=True, max_length=2048, null=True)),
                ('url', models.URLField(blank=True, max_length=512, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('CR', 'Created'), ('DP', 'Deployed'), ('AR', 'Archived')], default='CR', max_length=2)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model_owner', to='projects.Project')),
            ],
            options={
                'unique_together': {('name', 'version', 'project')},
            },
            managers=[
                ('objects_version', django.db.models.manager.Manager()),
            ],
        ),
    ]