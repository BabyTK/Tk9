# Generated by Django 3.1 on 2021-01-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210110_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Ürün Fotoğrafı'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Ürün Fotoğrafı 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Ürün Fotoğrafı 3'),
        ),
    ]
