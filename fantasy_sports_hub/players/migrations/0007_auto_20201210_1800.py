# Generated by Django 3.1.1 on 2020-12-10 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20201210_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nflplayer',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nflplayer',
            name='draft_round',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nflplayer',
            name='jersey_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nflplayer',
            name='number_drafted_overall',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nflplayer',
            name='year_drafted',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
