# Generated by Django 5.1.3 on 2024-12-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_estimates'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gallery_photo',
            field=models.ImageField(blank=True, null=True, upload_to='gallery', verbose_name='Фото в галерее'),
        ),
        migrations.AddField(
            model_name='project',
            name='is_in_gallery',
            field=models.ImageField(default=False, upload_to='', verbose_name='Отображается в галерее'),
        ),
        migrations.AddField(
            model_name='project',
            name='is_the_best',
            field=models.BooleanField(default=False, verbose_name='Входит в топ'),
        ),
    ]
