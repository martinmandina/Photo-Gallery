# Generated by Django 3.1.3 on 2020-11-15 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('photos', models.ImageField(upload_to='photos/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.location')),
            ],
        ),
    ]
