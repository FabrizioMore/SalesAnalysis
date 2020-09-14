from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        User_nombre = request.POST['nombre']
        User_email = request.POST['email']
        User_password = request.POST['password']
        
        user = User.objects.create_user(nombre=nombre, password=password,email=email)
        user.save();
        print('User created!')
        return redirect('/')
    else:
        return render(request,'login/index.html')

#def index(request):
#    context = {'insert_me':'Hello I am from login/index.html'}
#    return render(request,'login/index.html',context=context)
