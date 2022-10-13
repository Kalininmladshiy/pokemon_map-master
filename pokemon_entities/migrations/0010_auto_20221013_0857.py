# Generated by Django 2.2.24 on 2022-10-13 08:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20221013_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 13, 8, 57, 36, 747886, tzinfo=utc), null=True, verbose_name='когда появился'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 13, 8, 57, 36, 747956, tzinfo=utc), null=True, verbose_name='когда пропал'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(blank=True, null=True, verbose_name='широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(blank=True, null=True, verbose_name='долгота'),
        ),
    ]
