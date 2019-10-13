from django.urls import path,include
from quizbox import views
from django.conf.urls import url

app_name='quizbox'

urlpatterns=[
   path('game/',views.game,name='game'),
   path('end/',views.end,name='end'),
   path('highscores/',views.highscores,name='highscores'),
]
