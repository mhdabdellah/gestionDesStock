# Generated by Django 2.2.27 on 2022-02-24 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0042_facture_qte'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture',
            name='qte',
        ),
    ]
