# Generated by Django 5.1.3 on 2024-12-17 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_alter_request_name_alter_request_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Политика конфиденциальности', max_length=80, verbose_name='Политика конфиденциальности')),
            ],
            options={
                'verbose_name': 'Политика конфиденциальности',
                'verbose_name_plural': 'Политика конфиденциальности',
            },
        ),
        migrations.CreateModel(
            name='PrivacyPolicyParagraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('privacy_policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='contacts.privacypolicy', verbose_name='Политика конфиденциальности')),
            ],
        ),
    ]
