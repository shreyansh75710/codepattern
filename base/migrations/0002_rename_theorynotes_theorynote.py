# Generated by Django 3.2.8 on 2022-02-04 05:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='theoryNotes',
            new_name='theoryNote',
        ),
    ]
