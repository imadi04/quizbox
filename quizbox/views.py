from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'quizbox/index.html')

def end(request):
    return render(request,'quizbox/end.html')

def game(request):
    return render(request,'quizbox/game.html')

def highscores(request):
    return render(request,'quizbox/highscores.html')
