# Generated by Django 2.2.4 on 2019-08-23 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nps', '0004_nps_now'),
    ]

    operations = [
        migrations.AddField(
            model_name='nps',
            name='past',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
