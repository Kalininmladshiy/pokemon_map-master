# Generated by Django 2.2.24 on 2022-10-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20221014_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(blank=True, null=True, verbose_name='защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, null=True, verbose_name='здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, null=True, verbose_name='уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, null=True, verbose_name='выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(blank=True, null=True, verbose_name='сила'),
        ),
    ]
