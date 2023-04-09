from django.contrib import admin
from .models import Participants, User, Player, Match, Team, Contest

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'balance' , 'password')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'points')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'match')

@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('name', 'entry_fee', 'prize_pool', 'max_teams','match')
    
@admin.register(Participants)
class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('p1', 'p2','p1_logo','p2_logo')
