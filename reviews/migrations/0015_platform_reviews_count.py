# Generated by Django 5.1.3 on 2024-12-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_platform_average_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='reviews_count',
            field=models.IntegerField(default=0, verbose_name='Количество отзывов'),
        ),
    ]