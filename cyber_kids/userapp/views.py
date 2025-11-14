from django.shortcuts import render,redirect
from django.contrib import messages
from adminapp.models import AddGameModel,AddQuestions
from userapp.models import UserModel,FeedbackModel,Analysis
from textblob import TextBlob
import random

# Create your views here.

def user_dashboard(request):
    return render(request,'user/user-dashboard.html')

def user_feedback(request):
    user_id = request.session['user_id']
    u = UserModel.objects.get(user_id = user_id)
    all = FeedbackModel.objects.all().order_by('-feedback_id')
    if request.method == "POST":
        feedback = request.POST.get('comment')
        analysis = TextBlob(feedback)
        sentiment = ''
        if analysis.polarity >= 0.5:
            sentiment = 'Very Positive'
        elif analysis.polarity > 0 and analysis.polarity < 0.5:
            sentiment = 'Positive'
        elif analysis.polarity < 0 and analysis.polarity >= -0.5:
            sentiment = 'Negitive'
        elif analysis.polarity <= -0.5:
            sentiment = 'Very Negitive'
        else:
            sentiment = 'Neutral'

        FeedbackModel.objects.create(feedback=feedback,user = u,sentiment=sentiment)
        messages.success(request,'Feedback Submitted')
    return render(request,'user/user-feedback.html',{'feedback':all})

def games(request):
    games = AddGameModel.objects.all().order_by('-game_id')
    return render(request,'user/games.html',{'g':games})

def questions(request,id):
    que =list(AddQuestions.objects.all())

    random_item = random.choice(que)
    
    if request.method == 'POST':
        q_id = request.POST.get('q_id')
        check = request.POST.get('check')
        obj = AddQuestions.objects.get(pk=q_id)
        if check == obj.answer:
            correct,created = Analysis.objects.get_or_create(pk=1)
            correct.correct +=1
            correct.save()
            print(check,'matched')
            messages.success(request,'Access Granted Play now')
            return redirect('play_game',id=id)
        else:
            wrong,created = Analysis.objects.get_or_create(pk=1)
            wrong.wrong +=1
            wrong.save()
            print(check,'not matched')
            messages.error(request,'Access denied toPlay')
            return redirect('question',id=id)


    context = {
        'questions':random_item
    }
    return render(request,'user/quiz.html',context)

def play_game(request,id):
    game = AddGameModel.objects.get(pk=id)
    context = {
        'game':game
    }
    return render(request,'user/play_game.html',context)


def logout(request):
    messages.success(request,'Successfully Logged Out')
    return redirect('main_index')