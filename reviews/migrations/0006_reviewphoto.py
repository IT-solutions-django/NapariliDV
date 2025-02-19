# Generated by Django 5.1.3 on 2024-12-19 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_review_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Фото отзыва')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.review', verbose_name='Отзыв')),
            ],
        ),
    ]
