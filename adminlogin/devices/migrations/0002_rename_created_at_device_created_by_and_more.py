# Generated by Django 5.1.4 on 2024-12-12 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='created_at',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='updated_at',
            new_name='updated_by',
        ),
    ]
