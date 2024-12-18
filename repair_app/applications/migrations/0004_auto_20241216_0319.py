# Generated by Django 3.2.16 on 2024-12-16 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20241212_0100'),
        ('applications', '0003_rename_total_coast_application_total_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='components',
        ),
        migrations.RemoveField(
            model_name='application',
            name='services',
        ),
        migrations.RemoveField(
            model_name='application',
            name='total_cost',
        ),
        migrations.AddField(
            model_name='application',
            name='email',
            field=models.EmailField(default='ex@ex.com', max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='comment',
            field=models.TextField(blank=True, help_text='Необязательное поле', max_length=512, verbose_name='Описание проблемы'),
        ),
        migrations.CreateModel(
            name='ApplicationServiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1, verbose_name='Количество')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_items', to='applications.application')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='catalog.service')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationComponentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1, verbose_name='Количество')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='component_items', to='applications.application')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='component', to='catalog.component')),
            ],
        ),
    ]
