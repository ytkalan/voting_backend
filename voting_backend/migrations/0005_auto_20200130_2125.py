# Generated by Django 2.1.1 on 2020-01-30 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting_backend', '0004_auto_20200130_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voterecord',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_set', to='voting_backend.VoteCampaign'),
        ),
        migrations.AlterField(
            model_name='voterecord',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_set', to='voting_backend.VoteOption'),
        ),
    ]
