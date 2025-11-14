from django.shortcuts import render,redirect,get_object_or_404
from adminapp.models import AddGameModel, AddQuestions,Answers
from django.contrib import messages
from userapp.models import UserModel,Analysis,FeedbackModel
from django.core.paginator import Paginator

# Create your views here.

def admin_dashboard(request):
    users = UserModel.objects.all().count()
    games = AddGameModel.objects.all().count()
    questions = AddQuestions.objects.all().count()
    
    context = {
        'users':users,
        'games':games,
        'questions':questions,
        
    }
    return render(request,'admin/admin-dashboard.html',context)

def add_game(request):
    if request.method == "POST" and "image" in request.FILES:
        game_title = request.POST.get('title')
        gametype = request.POST.get('type')
        gameplatform = request.POST.get('platform')
        image = request.FILES['image']
        gameurl = request.POST.get('url')

        AddGameModel.objects.create(
            game_title = game_title,
            game_type=gametype,
            game_platform=gameplatform,
            game_image=image,
            game_url=gameurl
        )
        messages.success(request,'Game Added Successfully')
        return redirect('add_game')
    return render(request,'admin/add-game.html')

def manage_games(request):
    games = AddGameModel.objects.all().order_by('-game_id')

    paginator = Paginator(games,4)
    page_no = request.GET.get('page')
    page = paginator.get_page(page_no)
    return render(request,'admin/manage-game.html',{'game':page})

def delete_game(request,id):
    dd = AddGameModel.objects.get(pk=id)
    dd.delete()
    messages.success(request,'Deleted Successfully')
    return redirect('manage_games')

def edit_game(request,id):
    edit  = AddGameModel.objects.get(pk=id)
    if request.method == "POST":
        title = request.POST.get('title')
        type = request.POST.get('type')
        platform = request.POST.get('platform')
        url = request.POST.get('url')

        if not request.FILES.get('image',False):
            edit.game_title=title
            edit.game_type=type
            edit.game_platform=platform
            edit.game_url=url
        if request.FILES.get('image',False):
            image = request.FILES['image']
            edit.game_title=title
            edit.game_type=type
            edit.game_platform=platform
            edit.game_url=url
            edit.game_image = image
        edit.save()
        messages.success(request,'Updated Successfully')
        return redirect('edit_game',id)
    context = {
        'edit':edit
        }
    return render(request,'admin/edit-game.html',context)

def user_details(request):
    user = UserModel.objects.all().order_by('-user_id')
    context = {
        "users":user
    }
    return render(request,'admin/user-details.html',context)

def user_delete(request,id):
    user = UserModel.objects.get(pk=id)
    user.delete()
    messages.success(request,'User deleted successfully')
    return redirect('user_details')


def add_questions(request):
    if request.method =='POST':
        question = request.POST.get('question')
        option_1 = request.POST.get('option1')
        option_2 = request.POST.get('option2')
        option_3 = request.POST.get('option3')
        option_4 = request.POST.get('option4')
        check = request.POST.get('check')
        print(check,type(check),'fdfff')
       
        if check == '1':
            answer = option_1

        elif check == '2':
            answer = option_2
        
        elif check == '3':
            answer = option_3
            print('3')
        else:
            answer = option_4
            print('4')
        print(answer)
        try:
            question =  AddQuestions.objects.create(
                questions=question,
                option1 = option_1,
                option2 = option_2,
                option3 = option_3,
                option4 = option_4,
                answer = answer
            )
            
            Answers.objects.create(
                question = question,
                answer = question.answer
            )

            messages.success(request,'Question Add successfully')
            return redirect('add_questions')
        except:
            messages.error(request,'Question Add successfully')
            return redirect('add_questions')
    return render(request,'admin/Add-question-to-game.html')

def manage_questions(request):
    questions = AddQuestions.objects.all().order_by('-q_id')

    paginator = Paginator(questions,3)
    page_no = request.GET.get('page')
    page = paginator.get_page(page_no)

    context = {
        "questions":page
    }
    return render(request,'admin/manage_questions.html',context)

def edit_question(request,id):
    question = AddQuestions.objects.get(q_id=id)
    edit = get_object_or_404(AddQuestions,q_id=id)
    
    if request.method=='POST':
        question = request.POST.get('question')
        option_1 = request.POST.get('option1')
        option_2 = request.POST.get('option2')
        option_3 = request.POST.get('option3')
        option_4 = request.POST.get('option4')
        answer = request.POST.get('answer')
        check = request.POST.get('check')
        print(option_1)
        print(option_2)
        print(check)

       
        if request.POST.get('question',False):
            edit.questions  = question
            edit.option1 = option_1
            edit.option2 = option_2
            edit.option3 = option_3
            edit.option4 = option_4
            if check == '1':
                edit.answer = option_1

            elif check == '2':
                edit.answer = option_2
        
            elif check == '3':
                edit.answer = option_3
                print('3')
            else:
                edit.answer = option_4
                print('4')
          

        edit.save()
        messages.success(request,'Question edited successfully')
        return redirect('edit_questions',id=id)

    context= {
        "question":question
    }

    return render(request,'admin/edit_questions.html',context)

def delete_question(request,id):
    question = AddQuestions.objects.get(q_id=id)
    question.delete()
    messages.success(request,'Question deleted successfully')
    return redirect('manage_questions')

def cyber_kids_analysis(request):
    result = Analysis.objects.all().first()
    feedback = FeedbackModel.objects.all().count()
    correct = result.correct
    wrong = result.wrong
    print(correct)
    print(wrong)

    context = {
        'correct':correct,
        'wrong':wrong,
        'feedback' :feedback
    }
    return render(request,'admin/cyber-kids-analysis.html',context)

def feedback_management(request):
    feedback = FeedbackModel.objects.all().order_by('-feedback_id')
    paginator = Paginator(feedback,4)
    page_no = request.GET.get('page')
    page = paginator.get_page(page_no)

    context = {
        'feedback':page
    }
    return render(request,'admin/feedback-management.html',context)

def admin_logout(request):
    messages.success(request,'Admin Logout successfully ')
    return redirect('main_index')