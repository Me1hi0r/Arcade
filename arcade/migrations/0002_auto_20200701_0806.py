# Generated by Django 3.0.5 on 2020-07-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arcade', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='maze_games_count',
        ),
        migrations.RemoveField(
            model_name='player',
            name='maze_score_all_time',
        ),
        migrations.RemoveField(
            model_name='player',
            name='maze_score_day',
        ),
        migrations.AddField(
            model_name='player',
            name='scores',
            field=models.CharField(default='', max_length=600),
        ),
    ]
