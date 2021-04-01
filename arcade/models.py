from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=30)
    id_card = models.CharField(max_length=20)
    balance = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    faces_score_day = models.IntegerField(default=0)
    faces_games_count = models.IntegerField(default=0)
    
    harp_score_day = models.IntegerField(default=0)
    harp_games_count = models.IntegerField(default=0)

    triangle_score_day = models.IntegerField(default=0)
    triangle_games_count = models.IntegerField(default=0)

    tags_score_day = models.IntegerField(default=0)
    tags_games_count = models.IntegerField(default=0)

    bowman_score_day = models.IntegerField(default=0)
    bowman_games_count = models.IntegerField(default=0)

    color_memory_score_day = models.IntegerField(default=0)
    color_memory_games_count = models.IntegerField(default=0)

    cube_score_day = models.IntegerField(default=0)
    cube_games_count = models.IntegerField(default=0)

    tubes_score_day = models.IntegerField(default=0)
    tubes_games_count = models.IntegerField(default=0)

    castle_score_day = models.IntegerField(default=0)
    castle_games_count = models.IntegerField(default=0)

    holes_score_day = models.IntegerField(default=0)
    holes_games_count = models.IntegerField(default=0)

    memory_score_day = models.IntegerField(default=0)
    memory_games_count = models.IntegerField(default=0)

    maze_score_day = models.IntegerField(default=0)
    maze_games_count = models.IntegerField(default=0)
    
    tower_score_day = models.IntegerField(default=0)
    tower_games_count = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.username}'
