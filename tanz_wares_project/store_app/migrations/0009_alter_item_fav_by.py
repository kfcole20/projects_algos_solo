# Generated by Django 3.2.6 on 2021-09-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0008_alter_item_fav_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='fav_by',
            field=models.ManyToManyField(related_name='fav_item', to='store_app.User'),
        ),
    ]