# Generated by Django 5.1.5 on 2025-02-10 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserProfile',
        ),
    ]
