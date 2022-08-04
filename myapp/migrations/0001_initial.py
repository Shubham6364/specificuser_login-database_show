# Generated by Django 4.0.3 on 2022-08-04 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=200, null=True)),
                ('pwd', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specific',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200, null=True)),
                ('sname', models.CharField(max_length=300, null=True)),
                ('usernanme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.signup')),
            ],
        ),
    ]
