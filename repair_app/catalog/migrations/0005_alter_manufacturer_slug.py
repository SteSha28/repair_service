# Generated by Django 3.2.16 on 2024-12-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_manufacturer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='slug',
            field=models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', unique=True, verbose_name='Идентификатор'),
        ),
    ]