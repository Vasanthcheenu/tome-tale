from django.shortcuts import redirect, render
from .forms import SignUp
from .models import Category, Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your views here.
def web(request):
    return render(request,'navbar.html')
def footer(request):
    return render(request,'footer.html')
def home(request):
    Products=Product.objects.all()
    return render(request,'home.html',{'Products':Products})

def about(request):
    return render(request,'about.html')
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("You have been logged in "))
            return redirect('home')
        else:
            messages.success(request,("There is an error ,please try again"))
            return redirect('login')
    else:
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out"))
    return redirect('home')

def detail(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'details.html',{'product':product})

def category(request,foo):
    foo=foo.replace('-',' ')
    try:
        category=Category.objects.get(name=foo)
        products=Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products,'category':category})
    except:
        messages.success(request,("category not found"))
        return redirect('home')

def register_user(request):
    form = SignUp()
    if request.method =="POST":
        form=SignUp(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("Registered Successfully"))
            return redirect('home')
        else:
            messages.success(request,("Whoops! There is something went wrong ,please try again"))
            return redirect('register')
    else: 
        return render(request,'register.html',{'form':form})

def contact(request):
    return render(request,'contact.html')

def wishlist(request):
    return render(request,'wishlist.html')