# Generated by Django 3.2.16 on 2024-12-15 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_auto_20241215_0551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='total_coast',
            new_name='total_cost',
        ),
    ]
