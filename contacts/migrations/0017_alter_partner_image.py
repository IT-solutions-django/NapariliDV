# Generated by Django 5.1.3 on 2025-01-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0016_partner_delete_partnerimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.FileField(upload_to='contacts/certificates', verbose_name='Фото'),
        ),
    ]
