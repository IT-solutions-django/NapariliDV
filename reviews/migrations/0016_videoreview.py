# Generated by Django 5.1.3 on 2024-12-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0015_platform_reviews_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Видео')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('created_at', models.DateTimeField(verbose_name='Дата и время публикации')),
            ],
            options={
                'verbose_name': 'Видео отзыв',
                'verbose_name_plural': 'Видео отзывы',
                'ordering': ['-created_at'],
            },
        ),
    ]
