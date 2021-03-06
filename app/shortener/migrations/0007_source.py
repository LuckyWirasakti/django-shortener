# Generated by Django 3.1.7 on 2021-03-14 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0006_auto_20210314_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.URLField(max_length=500, verbose_name='reference')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='dibuat')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='terakhir diperbaharui')),
                ('shortener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener.shortener')),
            ],
            options={
                'verbose_name': 'source',
                'verbose_name_plural': 'sources',
            },
        ),
    ]
