# Generated by Django 5.2.1 on 2025-05-30 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='features',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='img',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='model',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='name',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='price',
        ),
    ]
