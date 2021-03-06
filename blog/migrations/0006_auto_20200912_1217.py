# Generated by Django 3.0.7 on 2020-09-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200912_1211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inline_editor',
            options={'ordering': ['order_num']},
        ),
        migrations.AlterModelOptions(
            name='post_gallery',
            options={'ordering': ['order_num']},
        ),
        migrations.AddField(
            model_name='inline_editor',
            name='order_num',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post_gallery',
            name='order_num',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
