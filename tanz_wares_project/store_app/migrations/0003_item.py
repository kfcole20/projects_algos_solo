# Generated by Django 3.2.6 on 2021-09-08 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_rename_password_user_pw'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.FloatField()),
                ('desc', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='images')),
            ],
        ),
    ]
