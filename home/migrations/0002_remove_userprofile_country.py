# Generated by Django 3.1 on 2021-01-10 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
    ]
