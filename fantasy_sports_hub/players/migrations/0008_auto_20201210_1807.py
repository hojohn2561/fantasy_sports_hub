# Generated by Django 3.1.1 on 2020-12-10 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_auto_20201210_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nflplayer',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nflplayer',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
