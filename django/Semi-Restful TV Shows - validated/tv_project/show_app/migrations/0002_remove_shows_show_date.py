# Generated by Django 2.2.4 on 2023-06-08 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shows',
            name='show_date',
        ),
    ]
