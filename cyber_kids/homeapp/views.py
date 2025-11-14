from django.shortcuts import render,redirect
from django.contrib import messages
from userapp.models import UserModel
# Create your views here.

def main_index(request):
    return render(request,'home/main-index.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    return render(request,'home/contact.html')

def admin_login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')

        if name == 'admin' and password == 'admin':
            messages.success(request,'Logged In Successfully')
            return redirect('admin_dashboard')
        else:
            messages.info(request,'invalid credentails')
            return redirect('admin_login')

    return render(request,'home/admin-login.html')
        
def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            check = UserModel.objects.get(user_email = email, user_password = password)
            request.session["user_id"] = check.user_id
            messages.success(request,'Login Successfully')
            return redirect('user_dashboard')
        except:
            messages.info(request,'Login Failed')
            return redirect('user_login')
    return render(request,'home/user-login.html')
 
def user_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        age = request.POST.get('age')

        UserModel.objects.create(user_name=name,
                                 user_email=email,
                                 user_password=password,
                                 user_age = age
                                 )
        messages.success(request,'Registered Successfully')
        return redirect('user_login')
    return render(request,'home/user-register.html')