# Generated by Django 3.1.7 on 2021-03-13 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='url',
            field=models.URLField(max_length=500, verbose_name='url'),
        ),
    ]
