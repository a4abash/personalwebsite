# Generated by Django 3.2.9 on 2023-08-24 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webmodels', '0015_rename_projectimage_projectimage_relatedproject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='image',
            new_name='mainimage',
        ),
    ]