# Generated by Django 4.0.5 on 2022-08-01 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_specific_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specific',
            name='signup',
            field=models.ForeignKey(default='signup', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.signup'),
        ),
    ]