# Generated by Django 5.1.3 on 2024-12-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_alter_galleryphoto_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='request',
            name='phone',
            field=models.CharField(max_length=18, verbose_name='Телефон'),
        ),
    ]
