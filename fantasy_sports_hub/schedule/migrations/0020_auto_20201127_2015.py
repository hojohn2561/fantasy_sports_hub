# Generated by Django 3.1.1 on 2020-11-28 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0019_auto_20201127_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='away_team',
            new_name='away_team_id',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='home_team',
            new_name='home_team_id',
        ),
    ]