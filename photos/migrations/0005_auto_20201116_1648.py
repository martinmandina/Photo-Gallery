# Generated by Django 3.1.3 on 2020-11-16 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20201115_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='photos',
            new_name='address',
        ),
    ]