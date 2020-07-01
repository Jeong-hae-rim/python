# Generated by Django 2.2.13 on 2020-07-01 09:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='download_users',
            field=models.ManyToManyField(related_name='download_apis', to=settings.AUTH_USER_MODEL),
        ),
    ]
