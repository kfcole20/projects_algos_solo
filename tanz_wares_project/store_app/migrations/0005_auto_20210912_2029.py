# Generated by Django 3.2.6 on 2021-09-13 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='fav_by',
            field=models.ManyToManyField(default='', related_name='fav_item', to='store_app.User'),
        ),
        migrations.AddField(
            model_name='item',
            name='purchase_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='purchased_item', to='store_app.user'),
        ),
    ]