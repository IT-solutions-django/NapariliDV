# Generated by Django 5.1.3 on 2024-12-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_cooperationstage_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperationstage',
            name='number',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Порядковый номер'),
        ),
    ]
