# Generated by Django 3.2.16 on 2022-10-28 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footballapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='football',
            old_name='Team_name',
            new_name='team_name',
        ),
    ]
