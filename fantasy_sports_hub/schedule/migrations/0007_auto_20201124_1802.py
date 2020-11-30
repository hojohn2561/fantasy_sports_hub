# Generated by Django 3.1.1 on 2020-11-24 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20200912_2205'),
        ('schedule', '0006_auto_20201116_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='away_team',
            field=models.ManyToManyField(
                related_name='away_team', to='teams.nflteam'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='home_team',
            field=models.ManyToManyField(
                related_name='home_team', to='teams.nflteam'),
        ),
    ]
