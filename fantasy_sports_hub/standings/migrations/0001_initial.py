# Generated by Django 3.1.1 on 2020-09-15 00:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0004_auto_20200912_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standing',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('season_year', models.PositiveIntegerField(
                    verbose_name=django.core.validators.MaxValueValidator(2400))),
                ('league', models.CharField(max_length=50)),
                ('conference', models.CharField(max_length=50)),
                ('division', models.CharField(max_length=50)),
                ('conference_rank', models.PositiveIntegerField()),
                ('division_rank', models.PositiveIntegerField()),
                ('wins', models.PositiveIntegerField()),
                ('losses', models.PositiveIntegerField()),
                ('ties', models.PositiveIntegerField()),
                ('win_percentage', models.FloatField()),
                ('streak', models.CharField(max_length=5)),
                ('conference_wins', models.PositiveIntegerField()),
                ('conference_losses', models.PositiveIntegerField()),
                ('conference_ties', models.PositiveIntegerField()),
                ('non_conference_wins', models.PositiveIntegerField()),
                ('non_conference_losses', models.PositiveIntegerField()),
                ('non_conference_ties', models.PositiveIntegerField()),
                ('division_wins', models.PositiveIntegerField()),
                ('division_losses', models.PositiveIntegerField()),
                ('division_ties', models.PositiveIntegerField()),
                ('non_division_wins', models.PositiveIntegerField()),
                ('non_division_losses', models.PositiveIntegerField()),
                ('non_division_ties', models.PositiveIntegerField()),
                ('points_for', models.PositiveIntegerField()),
                ('points_against', models.PositiveIntegerField()),
                ('points_diff', models.IntegerField()),
                ('home_wins', models.PositiveIntegerField()),
                ('home_losses', models.PositiveIntegerField()),
                ('road_wins', models.PositiveIntegerField()),
                ('road_losses', models.PositiveIntegerField()),
                ('team', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='teams.nflteam')),
            ],
        ),
    ]
