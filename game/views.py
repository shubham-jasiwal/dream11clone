from msilib.schema import ListView
from django.shortcuts import get_object_or_404, render



from django.shortcuts import render
from .models import Contest, Match, Player, Team

app_name = 'game'

def contest_list(request):
    contests = Contest.objects.all()
    return render(request, 'contests.html', {'contests': contests})


def home(request):
    # Your view code goes here
    return render(request, 'home.html')


def account(request):
    return render(request, 'account.html')

def leaderboard(request):
    teams = Team.objects.all()
    return render(request, 'leaderboard.html', {'teams': teams})

def contest_detail(request, pk):
    contest = Contest.objects.get(pk=pk)
    players = contest.match.players.all()
    return render(request, 'create_team.html', {'players': players,'contest': contest})

def match_list(request):
    matches = Match.objects.all()
    context = {
        'matches': matches
    }
    return render(request, 'matches.html', context)

def match_contests(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    contests = Contest.objects.filter(match=match)
    return render(request, 'match_contests.html', {'match': match, 'contests': contests})



def create_team(request):
    if request.method == 'POST':
        team_name = request.POST['team_name']
        contest = request.POST['contest']
        contest=Contest.objects.get(pk=int(contest))
        match = contest.match
        selected_players = request.POST.getlist('players')
        team = Team.objects.create(name=team_name,Contest=contest, match=match)
        for player_id in selected_players:
            player = Player.objects.get(id=player_id)
            team.players.add(player)
        return render(request, 'team_created.html', {'team': team})
    else:
        return render(request, 'create_team.html',)


