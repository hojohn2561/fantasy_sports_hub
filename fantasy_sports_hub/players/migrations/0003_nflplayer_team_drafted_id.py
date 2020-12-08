# Generated by Django 3.1.1 on 2020-12-08 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20201130_1336'),
        ('players', '0002_nflplayer_current_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='nflplayer',
            name='team_drafted_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_drafted', to='teams.nflteam'),
        ),
    ]