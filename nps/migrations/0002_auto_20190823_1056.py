# Generated by Django 2.2.4 on 2019-08-23 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nps',
            name='asset_rate',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='nps',
            name='share',
            field=models.CharField(max_length=5),
        ),
    ]
