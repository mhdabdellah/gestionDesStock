# Generated by Django 3.2.2 on 2021-08-30 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0023_auto_20210830_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture',
            name='article',
        ),
        migrations.AlterField(
            model_name='sortir',
            name='date_sortie',
            field=models.DateField(blank=True, null=True),
        ),
    ]