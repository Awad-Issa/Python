# Generated by Django 2.2.4 on 2023-06-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_app', '0007_remove_shows_show_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='show_date',
            field=models.DateField(default=None),
        ),
    ]
