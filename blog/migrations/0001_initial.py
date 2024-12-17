# Generated by Django 5.1.3 on 2024-12-17 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Тип статьи')),
            ],
            options={
                'verbose_name': 'Тип статьи',
                'verbose_name_plural': 'Типы статей',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')),
                ('image', models.ImageField(null=True, upload_to='articles', verbose_name='Фото')),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('article_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.articletype', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Блог',
            },
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Картинка')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article', verbose_name='Статья/Новость')),
            ],
        ),
    ]
