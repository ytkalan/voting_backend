# Generated by Django 2.1.1 on 2020-01-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_backend', '0003_auto_20200130_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voteoption',
            old_name='option',
            new_name='option_code',
        ),
        migrations.AddField(
            model_name='voteoption',
            name='option_detail',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='voteoption',
            unique_together={('campaign', 'option_code')},
        ),
    ]
