# Generated by Django 3.1.1 on 2020-12-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20201210_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='nflplayer',
            name='status',
            field=models.CharField(default='', max_length=50),
        ),
    ]