# Generated by Django 3.0.5 on 2020-07-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arcade', '0002_auto_20200701_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='scores',
            field=models.CharField(default="{'faces': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}, 'harp': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}, 'triangle': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}, 'tags': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}, 'bowman': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}, 'color_memory': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}, 'cube': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}, 'tubes': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}, 'castle': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}, 'holes': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}, 'memory': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}, 'maze': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}, 'tower': {'all_scores': 0, 'day_scores': 0, 'play_games': 0}}", max_length=2000),
        ),
    ]
