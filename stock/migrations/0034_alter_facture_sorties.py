# Generated by Django 3.2.2 on 2021-09-13 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0033_remove_stock_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='sorties',
            field=models.ManyToManyField(blank=True, related_name='sorties', to='stock.Sortir'),
        ),
    ]
