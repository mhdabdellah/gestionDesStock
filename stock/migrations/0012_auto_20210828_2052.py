# Generated by Django 3.2.2 on 2021-08-28 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_alter_article_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='statut',
            field=models.CharField(choices=[('0', 'Oui'), ('1', 'Non')], default='0', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='categorie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stock.categorie'),
            preserve_default=False,
        ),
    ]
