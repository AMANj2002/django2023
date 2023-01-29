# Generated by Django 4.1.2 on 2023-01-29 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='uploads/product/1_01.jpg', upload_to='uploads/products1/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='uploads/product/1_01.jpg', upload_to='uploads/products2/'),
        ),
    ]
