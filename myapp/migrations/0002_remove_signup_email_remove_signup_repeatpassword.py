# Generated by Django 4.0.5 on 2022-08-04 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='email',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='repeatpassword',
        ),
    ]
