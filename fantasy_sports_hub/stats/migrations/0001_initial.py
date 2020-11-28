# Generated by Django 3.1.1 on 2020-11-28 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0004_auto_20200912_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='NflTeamRegularSeasonRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_year', models.PositiveIntegerField()),
                ('season_type', models.CharField(max_length=50)),
                ('win_count', models.PositiveSmallIntegerField(default=0)),
                ('loss_count', models.PositiveSmallIntegerField(default=0)),
                ('tie_count', models.PositiveSmallIntegerField(default=0)),
                ('team_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_id', to='teams.team')),
            ],
        ),
    ]
