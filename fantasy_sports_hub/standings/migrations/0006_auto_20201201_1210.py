# Generated by Django 3.1.1 on 2020-12-01 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standings', '0005_auto_20201101_2037'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Standing',
            new_name='NflStanding',
        ),
    ]
