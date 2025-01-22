from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Mobile,Todo


# Create your views here.

def home(request):
    return render(request,'home.html')

from django.contrib.auth.models import User 
def signupform(request):
    if request.method == "POST":
        firstname=request.POST['first_name']
        lastname=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        mobilenumber=request.POST['mnum']
        password=request.POST["password"]
        confirmpassword=request.POST["confirmpassword"]
        existing_user=User.objects.all()        

        if password == confirmpassword:
            person=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            Mobile.objects.create(mobile=mobilenumber,uid_id=person.id)
            messages.info(request,"succesfully Registered  "+ username) 
            return render(request,'signin.html')
    
    return render(request,'signup.html')

from django.contrib.auth import authenticate,login, logout

def signin(request):
    url=request.GET.get('next')
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in as " + username)
            if url:
                return redirect(url)
            return redirect('todo')
        else:
            messages.info(request,'Enter Valid Credentials')
            return render(request,'signup.html')
    return render(request,'signin.html')


def signout(request):
    logout(request)
    messages.info(request,"Successfully logged out ")
    return redirect('signin')


# @login_required(login_url='signin')
def todo(request):
    data=Todo.objects.filter(uid_id=request.user.id)
    if request.method=="POST":
        task=request.POST['task']
        date=request.POST['date']
        user_id=request.user.id
        

        Todo.objects.create(task=task,date=date,uid_id=user_id)
        return redirect('todo')
    return render(request,'todo.html',{'data':data})

def modify(request,id):
    if request.method=="POST":
        task=request.POST['task']
        date=request.POST['date']
        if task and date:
            Todo.objects.filter(id=id).update(task=task,date=date)
            return redirect('todo')
        if task and date == '':
            messages.info(request,'Enter Details')
            return redirect('todo')

        if task == '':
                pass
        else:Todo.objects.filter(id=id).update(task=task)
        
        if date == '':
            pass
        else:Todo.objects.filter(id=id).update(date=date)
        return redirect('todo')
    return render(request,'todo.html')

def delete(request,id):
    Todo.objects.filter(id=id).delete()
    return redirect('todo')

def completed(request,id):
    Todo.objects.filter(id=id).delete(status='completed')
    return redirect('todo')

def delete_completed(request,id):
    Todo.objects.filter(id=id).delete()
    return redirect('todo_completed')


def completeddata(request):
    data=Todo.objects.filter(uid_id=request.user.id)
    return render(request,"todo_completed.html",{'data':data})

