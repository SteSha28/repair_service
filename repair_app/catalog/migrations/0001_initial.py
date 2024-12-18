# Generated by Django 3.2.16 on 2024-12-10 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Тип техники')),
                ('slug', models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Производитель')),
                ('slug', models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=512, verbose_name='Наименование')),
                ('article_number', models.TextField(max_length=128, verbose_name='Артикул')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('comment', models.TextField(blank=True, help_text='Необязательное поле', max_length=512, verbose_name='Комментарий')),
                ('duration', models.DurationField(verbose_name='Продолжительность')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=512, verbose_name='Наименование')),
                ('article_number', models.TextField(max_length=128, verbose_name='Артикул')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('comment', models.TextField(blank=True, help_text='Необязательное поле', max_length=512, verbose_name='Комментарий')),
                ('quantity', models.IntegerField(verbose_name='Количество на складе')),
                ('availability', models.BooleanField(default=False, verbose_name='Наличие')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category', verbose_name='Категория')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.manufacturer', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'деталь',
                'verbose_name_plural': 'Детали',
            },
        ),
    ]
