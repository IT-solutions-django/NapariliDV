# Generated by Django 5.1.3 on 2024-12-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_companyfact_company_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooperationstage',
            name='number',
            field=models.SmallIntegerField(default=1, verbose_name='Порядковый номер'),
            preserve_default=False,
        ),
    ]