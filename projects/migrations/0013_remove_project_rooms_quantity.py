# Generated by Django 5.1.3 on 2025-01-16 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_alter_project_is_in_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='rooms_quantity',
        ),
    ]
