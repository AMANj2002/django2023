# Generated by Django 4.1.2 on 2023-01-29 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_rename_description_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=20),
        ),
    ]