# Generated by Django 3.2.6 on 2021-08-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date_entree',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='prix_achat',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='qtStock',
            field=models.IntegerField(null=True),
        ),
    ]
