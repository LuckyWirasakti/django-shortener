# Generated by Django 3.1.7 on 2021-03-14 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20210313_2305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortener',
            options={'verbose_name': 'Pemendek', 'verbose_name_plural': 'Pemendek'},
        ),
        migrations.AlterField(
            model_name='shortener',
            name='alias',
            field=models.SlugField(help_text='Nama pengganti alamat lebih ringkas', verbose_name='Pengganti'),
        ),
        migrations.AlterField(
            model_name='shortener',
            name='count',
            field=models.PositiveIntegerField(default=0, help_text='Nilai hitung hasil klik', verbose_name='hitung'),
        ),
        migrations.AlterField(
            model_name='shortener',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='dibuat'),
        ),
        migrations.AlterField(
            model_name='shortener',
            name='snippet',
            field=models.TextField(blank=True, help_text='Potongan kode untuk penggunaan analisa google/facebook', null=True, verbose_name='snippet'),
        ),
        migrations.AlterField(
            model_name='shortener',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='terakhir diperbaharui'),
        ),
        migrations.AlterField(
            model_name='shortener',
            name='url',
            field=models.URLField(help_text='Alamat asli', max_length=500, verbose_name='Alamat'),
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='dibuat')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='terakhir diperbaharui')),
                ('shortener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener.shortener')),
            ],
        ),
    ]
