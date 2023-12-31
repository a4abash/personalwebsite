# Generated by Django 3.2.9 on 2023-08-17 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webmodels', '0007_auto_20230817_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='active',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='images/blog.jpg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='subtitle',
            field=models.CharField(default='By Abash', max_length=200),
        ),
        migrations.CreateModel(
            name='Projectimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project/')),
                ('projectImage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webmodels.project')),
            ],
        ),
    ]
