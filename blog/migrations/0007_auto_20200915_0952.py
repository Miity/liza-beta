# Generated by Django 3.0.7 on 2020-09-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200912_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inline_editor',
            name='htmlclass',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='HTML Class'),
        ),
    ]
