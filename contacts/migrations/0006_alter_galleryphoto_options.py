# Generated by Django 5.1.3 on 2024-12-15 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_galleryphoto_request_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryphoto',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Галерея'},
        ),
    ]
