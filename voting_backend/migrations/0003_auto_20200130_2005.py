# Generated by Django 2.1.1 on 2020-01-30 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting_backend', '0002_auto_20200130_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voteoption',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_set', to='voting_backend.VoteCampaign'),
        ),
    ]
