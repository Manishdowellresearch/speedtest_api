# Generated by Django 4.0.5 on 2022-06-24 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speedresultapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speed_test_data',
            old_name='download_speed',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='speed_test_data',
            name='upload_speed',
        ),
    ]