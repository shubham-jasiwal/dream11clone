from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contests/', views.contest_list, name='contest_list'),
    path('contests/<int:pk>/', views.contest_detail, name='contest_detail'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('account/', views.account, name='account'),
    path('matches/', views.match_list, name='matches'),
    path('match/<int:match_id>/contests/', views.match_contests, name='match_contests'),
    path('create_team/', views.create_team, name='create_team')
]
