# Generated by Django 3.2.9 on 2023-08-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmodels', '0008_auto_20230817_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
