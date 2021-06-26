from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username = username, password = password) #유저가 존재하는지를 확인
            if user is not None:
                login(request, user)

        return redirect('home')


    else:
        form = AuthenticationForm()
        return render (request, 'accounts/login.html', {'form':form})



def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('success')
        
        return redirect('home')

    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form':form})



def home(request):
    return render(request, 'accounts/home.html')


def success(request):
    return render(request, 'accounts/success.html')

