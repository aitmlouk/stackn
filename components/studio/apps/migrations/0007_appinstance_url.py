# Generated by Django 2.2.13 on 2021-02-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_appinstance_keycloak_client_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinstance',
            name='url',
            field=models.CharField(max_length=512, null=True),
        ),
    ]