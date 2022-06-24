# Generated by Django 4.0.5 on 2022-06-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speedresultapp', '0002_rename_download_speed_speed_test_data_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speed_test_data',
            old_name='data',
            new_name='download_speed',
        ),
        migrations.AddField(
            model_name='speed_test_data',
            name='upload_speed',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]