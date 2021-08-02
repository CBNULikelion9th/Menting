#from Menting.accounts.models import CustomUser 오류 나서 주석처리 했습니다 (승하)
from django.http.response import HttpResponse
from .models import CustomUser ,University
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, UnivesityForm, Change_emailForm
from django.contrib import messages
from django.contrib.auth.views import  PasswordChangeView
from django.urls import reverse_lazy

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

def login_view(request):   #로그인 
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username = username, password = password) #유저가 존재하는지를 확인
            if user is not None: #유저가 존재할시 로그인 되고 홈으로 들어간다
                login(request, user)
                return redirect('main')
            else:
                messages.add_message(request, messages.INFO, '아이디와 비밀번호를 확인하세요!')
                return redirect('login')

        else: #아이디와 비밀번호를 입력하지 않으면 로그인 페이지를 돌려줌
            messages.add_message(request, messages.INFO, '아이디와 비밀번호를 확인하세요!')
            return redirect('login')
        
                


    else: #로그인 빈폼
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

    
def change_email(request):  
    userr = CustomUser.objects.get(username = request.user) 
    
    if request.method == 'POST':
        form = Change_emailForm(request.POST)
        if form.is_valid():
            userr.email = form.cleaned_data['email']
            userr.save()
            return render (request, 'accounts/change_emailsuccess.html')
        
        return HttpResponse('fail')

    else:
        form = Change_emailForm()

    return render (request, 'accounts/change_email.html',{'form':form})



class MyPasswordChangeView(PasswordChangeView):
    success_url=reverse_lazy('mypage')          #변경에 성공시 들어갈 페이지
    template_name='accounts/password_change_form.html'      #변경 페이지
    
    def form_valid(self, form):                     #변경하고 message를 이용해서 성공여부를 띄우는데 뜨지 않는다
        messages.info(self.request, '암호 변경을 완료했습니다.')
        return super().form_valid(form)
    