# Generated by Django 5.1.3 on 2024-12-15 02:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_privacypolicy_companyadvantage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='bathrooms_quantity',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Количество санузлов'),
        ),
        migrations.AddField(
            model_name='slide',
            name='bedrooms_quantity',
            field=models.SmallIntegerField(default=1, verbose_name='Количество спален'),
        ),
        migrations.AddField(
            model_name='slide',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slide',
            name='square',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Площадь'),
            preserve_default=False,
        ),
    ]