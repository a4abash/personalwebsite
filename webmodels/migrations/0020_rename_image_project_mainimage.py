# Generated by Django 3.2.9 on 2023-09-07 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webmodels', '0019_rename_mainimage_project_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='image',
            new_name='mainimage',
        ),
    ]