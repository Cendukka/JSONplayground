# Generated by Django 3.1.3 on 2020-11-22 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temperature',
            old_name='tempererature_c',
            new_name='temperature_c',
        ),
    ]
