# Generated by Django 3.2.9 on 2023-08-24 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmodels', '0017_remove_blog_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='webmodels.Tag'),
        ),
    ]
