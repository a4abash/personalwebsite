# Generated by Django 3.2.9 on 2023-08-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmodels', '0010_rename_post_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.ManyToManyField(to='webmodels.Blog')),
                ('tag_id', models.ManyToManyField(to='webmodels.Tag')),
            ],
        ),
    ]
