# Generated by Django 3.2.6 on 2021-09-08 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='pw',
        ),
    ]
