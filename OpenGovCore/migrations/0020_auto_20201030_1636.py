# Generated by Django 3.1 on 2020-10-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenGovCore', '0019_auto_20201029_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='date_of_introduction',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='debates',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]