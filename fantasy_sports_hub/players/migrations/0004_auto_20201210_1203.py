# Generated by Django 3.1.1 on 2020-12-10 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_nflplayer_team_drafted_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nflplayer',
            old_name='api_player_id',
            new_name='player_api_id',
        ),
    ]
