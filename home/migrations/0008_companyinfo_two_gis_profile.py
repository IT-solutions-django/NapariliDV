# Generated by Django 5.1.3 on 2024-12-17 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_companyinfo_full_name_companyinfo_inn_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='two_gis_profile',
            field=models.URLField(default='https://2gis.ru/vladivostok/firm/70000001059056448/tab/reviews', verbose_name='Ссылка на профиль в 2GIS'),
        ),
    ]