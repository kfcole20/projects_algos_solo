# Generated by Django 3.2.6 on 2021-09-13 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_remove_item_purchase_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='fav_by',
            field=models.ManyToManyField(default='', related_name='fav_item', to='store_app.User'),
        ),
    ]