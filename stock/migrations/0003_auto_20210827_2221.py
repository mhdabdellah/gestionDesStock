# Generated by Django 3.2.2 on 2021-08-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20210827_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='description',
        ),
        migrations.AddField(
            model_name='article',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
