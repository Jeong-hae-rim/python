# Generated by Django 2.1.15 on 2020-06-29 01:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=200)),
                ('api_url', models.CharField(max_length=200)),
                ('latest_modified_date', models.DateField()),
                ('copyright', models.CharField(max_length=100)),
                ('copyright_range', models.CharField(max_length=100)),
                ('api_file', models.CharField(max_length=100)),
                ('download_users', models.ManyToManyField(blank=True, null=True, related_name='download_apis', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]