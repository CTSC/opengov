# Generated by Django 3.1 on 2020-10-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenGovCore', '0013_auto_20201003_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bills',
            old_name='date',
            new_name='date_of_introduction',
        ),
        migrations.AddField(
            model_name='bills',
            name='debate_loksabha_date',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bills',
            name='debate_rajyasabha_date',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
