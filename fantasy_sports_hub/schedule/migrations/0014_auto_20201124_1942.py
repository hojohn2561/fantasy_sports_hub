# Generated by Django 3.1.1 on 2020-11-25 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20200912_2205'),
        ('schedule', '0013_auto_20201124_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='away_team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='teams.team'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='home_team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='teams.team'),
        ),
    ]