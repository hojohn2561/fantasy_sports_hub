# Generated by Django 3.1.1 on 2020-12-10 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_nflplayer_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nflplayer',
            old_name='number_drafted',
            new_name='number_drafted_overall',
        ),
    ]
