#from Menting.accounts.models import CustomUser 오류 나서 주석처리 했습니다 (승하)
from django.http.response import HttpResponse
from .models import CustomUser , University
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, UnivesityForm


def main(request): 

    if request.method == 'GET':
        a = UnivesityForm()

    else:
        a = UnivesityForm(request.POST)
        if a.is_valid():

            t = a
            
            return render (request,'main/universityname.html',{ 't': t })
        return HttpResponse('fail')

    return render (request, 'accounts/main.html', { 'a': a })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username = username, password = password) #유저가 존재하는지를 확인
            if user is not None:
                login(request, user)
                return redirect('main')

        else:
            messages.add_message(request, messages.INFO, '아이디와 비밀번호를 확인하세요!')
            return redirect('login')
        
                


    else:
        form = AuthenticationForm()
        return render (request, 'accounts/login.html', {'form':form})



def logout_view(request):
    logout(request)
    return redirect('main')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        
        if form.is_valid():
            user = form.save()
            return redirect('success')



        else:
            messages.add_message(request, messages.INFO, '회원 가입에 실패 했습니다.')
            return redirect('signup')



    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form':form})




def success(request):
    return render(request, 'accounts/success.html')

def mypage(request):
    return render(request, 'accounts/mypage.html')

    

