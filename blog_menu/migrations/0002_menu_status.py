# Generated by Django 3.0.7 on 2020-10-19 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Опубликовать?'),
        ),
    ]
