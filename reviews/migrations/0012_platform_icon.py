# Generated by Django 5.1.3 on 2024-12-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_alter_reviewphoto_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='icon',
            field=models.ImageField(null=True, upload_to='reviews/platforms', verbose_name='Иконка'),
        ),
    ]
