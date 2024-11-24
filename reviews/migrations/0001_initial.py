# Generated by Django 5.1.3 on 2024-11-24 03:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwoGISReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('username', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('created_at', models.DateTimeField(verbose_name='Дата и время публикации')),
            ],
            options={
                'verbose_name': 'Отзыв с 2GIS',
                'verbose_name_plural': 'Отзывы с 2GIS',
                'ordering': ['-created_at'],
            },
        ),
    ]
