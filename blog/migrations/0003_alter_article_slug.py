# Generated by Django 5.1.3 on 2024-12-24 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_paragraph_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Слаг'),
        ),
    ]
