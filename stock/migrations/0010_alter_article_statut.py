# Generated by Django 3.2.2 on 2021-08-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_article_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='statut',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
