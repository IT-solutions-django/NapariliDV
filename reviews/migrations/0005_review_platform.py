# Generated by Django 5.1.3 on 2024-11-27 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='platform',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reviews.platform', verbose_name='Платформа'),
            preserve_default=False,
        ),
    ]
