# Generated by Django 3.2.7 on 2021-09-11 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0032_auto_20210910_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='nom',
        ),
    ]