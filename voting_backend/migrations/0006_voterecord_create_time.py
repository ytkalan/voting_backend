# Generated by Django 2.1.1 on 2020-02-01 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_backend', '0005_auto_20200130_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='voterecord',
            name='create_time',
            field=models.DateField(auto_now=True),
        ),
    ]
