# Generated by Django 3.2.7 on 2021-09-14 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0035_auto_20210914_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='profiles',
        ),
    ]
