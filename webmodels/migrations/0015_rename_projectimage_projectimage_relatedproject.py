# Generated by Django 3.2.9 on 2023-08-24 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webmodels', '0014_auto_20230821_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectimage',
            old_name='projectImage',
            new_name='relatedProject',
        ),
    ]
