# Generated by Django 3.2.6 on 2021-09-08 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0003_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='item_images'),
        ),
    ]
