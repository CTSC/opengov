# Generated by Django 3.1 on 2020-10-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenGovCore', '0017_auto_20201013_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parliamentary_constituencies',
            name='constituency_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]