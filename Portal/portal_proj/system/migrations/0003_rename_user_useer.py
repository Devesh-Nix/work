# Generated by Django 5.1.6 on 2025-02-09 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_remove_sale_created_by_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='useer',
        ),
    ]
