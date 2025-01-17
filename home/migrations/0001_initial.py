# Generated by Django 5.1.3 on 2024-11-24 02:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('history', models.TextField(verbose_name='История компании')),
                ('mission', models.TextField(verbose_name='Миссия компании')),
                ('address', models.CharField(max_length=120, verbose_name='Адрес')),
                ('working_mode', models.TextField(verbose_name='Режим работы')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('whatsapp', models.CharField(max_length=200, verbose_name='Ссылка на Whatsapp')),
                ('admin_panel_title', models.CharField(default='Информация о компании', max_length=40, verbose_name='Название вкладки в админке')),
            ],
            options={
                'verbose_name': 'Информация о компании',
                'verbose_name_plural': 'Информация о компании',
            },
        ),
        migrations.CreateModel(
            name='CooperationStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Название')),
                ('icon', models.FileField(upload_to='', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Этап сотрудничества',
                'verbose_name_plural': 'Этапы сотрудничества',
            },
        ),
        migrations.CreateModel(
            name='PopularQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150, verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=150, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='home/slides', verbose_name='Фото')),
                ('button_text', models.CharField(max_length=50, verbose_name='Надпись на кнопке')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
        migrations.CreateModel(
            name='CompanyFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('company_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facts', to='home.companyinfo', verbose_name='Информация о компании')),
            ],
            options={
                'verbose_name': 'Факт',
                'verbose_name_plural': 'Факты о компании',
            },
        ),
        migrations.CreateModel(
            name='CompanyAdvantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='home/company_advantages', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('company_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advantages', to='home.companyinfo', verbose_name='Преимущества компании')),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества компании',
            },
        ),
        migrations.CreateModel(
            name='CompanyService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('company_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='home.companyinfo', verbose_name='Услуги компании')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги компании',
            },
        ),
    ]
