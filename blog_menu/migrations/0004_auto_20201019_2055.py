# Generated by Django 3.0.7 on 2020-10-19 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_menu', '0003_auto_20201019_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='slug',
            new_name='url',
        ),
    ]
