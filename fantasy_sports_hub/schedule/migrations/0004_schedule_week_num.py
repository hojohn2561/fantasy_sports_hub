# Generated by Django 3.1.1 on 2020-11-06 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20201106_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='week_num',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
