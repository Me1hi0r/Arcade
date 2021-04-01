from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Player


def main(request):
    return render(request, 'arcade/start.html')

def check(request, card):
    try:
        p = Player.objects.filter(id_card=card).latest('id')
        return HttpResponse(f'{p.username}|{p.balance}|{p.id_card}')
    except ObjectDoesNotExist:
        return HttpResponse("new")

def change(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        card = request.POST.get('card')
        blnc = request.POST.get('balance')
        try:
            # p = Player.objects.get(id_card = card)
            p = Player.objects.filter(username = name).latest('id')
            p.username = name
            p.balance = blnc
            p.save()
            return HttpResponse("update")
        except ObjectDoesNotExist:
            p = Player(username=name, id_card=card, balance=blnc)
            p.save()
            return HttpResponse("create")

def validate(request, card):
    if request.method == 'GET':
        try:
            p = Player.objects.filter(id_card=card).latest('id')
            if p.balance:
                p.balance = p.balance - 1
                p.save()
                return HttpResponse("update")
            return HttpResponse("zero")
        except ObjectDoesNotExist:
            return HttpResponse("none")

def result(request):
    if request.method == 'POST':
        quest_name = request.POST.get('riddle')
        card = request.POST.get('card')
        score = request.POST.get('points')
        print(quest_name, card, score)
        try:
            # p = Player.objects.get(id_card = card)
            p = Player.objects.filter(id_card = card).latest('id')
            attr_score = quest_name + '_score_day'
            attr_count = quest_name + '_games_count'
            v = getattr(p, attr_count)
            setattr(p, attr_score, score)
            setattr(p, attr_count, v + 1)
            p.save()
            return HttpResponse("save")
        except ObjectDoesNotExist:
            return HttpResponse("none")


def leaderboard(request, quest):
    print(quest)
    # mqtt_routine()
    str_field = '-' + quest + '_score_day'
    game_list = list(Player.objects.all().order_by(str_field)[0:20])
    print(game_list)
    # print(game_list[0].str_field[1:])
    my_list = []
    for p in game_list:
        my_list.append([p.username, (getattr(p, str_field[1:]))])
    print(my_list)
    context  = {
        'quest_name': quest,
        'game_list': my_list,
    }
    return render(request, 'arcade/leaderboard.html', context)

def player(request, id_card):
    context = {}
    return HttpResponse("Here's the text of the Web page.")
    # if request.method == 'GET':
    #     try:
    #         p = Player.objects.get(id_card=id_card)
    #         context.update({
    #             'username': p.username,
    #             'balance': p.balance,

    #             'q1_name': 'faces',
    #             'q1_score': p.faces_score_day,
    #             'q1_games': p.faces_games_count,

    #             'q2_name': 'harp',
    #             'q2_score': p.harp_score_day,
    #             'q2_games': p.harp_games_count,

    #             'q3_name': 'triangle',
    #             'q3_score': p.triangle_score_day,
    #             'q3_games': p.triangle_games_count,

    #             'q4_name': 'tags',
    #             'q4_score': p.tags_score_day,
    #             'q4_games': p.tags_games_count,

    #             'q5_name': 'bowman',
    #             'q5_score': p.bowman_score_day,
    #             'q5_games': p.bowman_games_count,

    #             'q6_name': 'color memory',
    #             'q6_score': p.color_memory_score_day,
    #             'q6_games': p.color_memory_games_count,

    #             'q7_name': 'cube',
    #             'q7_score': p.cube_score_day,
    #             'q7_games': p.cube_games_count,

    #             'q8_name': 'tubes',
    #             'q8_score': p.tubes_score_day,
    #             'q8_games': p.tubes_games_count,

    #             'q9_name': 'castle',
    #             'q9_score': p.castle_score_day,
    #             'q9_games': p.castle_games_count,

    #             'q10_name': 'holes',
    #             'q10_score': p.holes_score_day,
    #             'q10_games': p.holes_games_count,

    #             'q11_name': 'memory',
    #             'q11_score': p.memory_score_day,
    #             'q11_games': p.memory_games_count,

    #             'q12_name': 'maze',
    #             'q12_score': p.maze_score_day,
    #             'q12_games': p.maze_games_count,

    #             'q13_name': 'tower',
    #             'q13_score': p.tower_score_day,
    #             'q13_games': p.tower_games_count,
    #         })
    #     except ObjectDoesNotExist:
    #         context.update({'NOT_EXIST': True})
    # return render(request, 'arcade/player.html', context)

