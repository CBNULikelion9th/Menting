#from Menting.accounts.models import CustomUser 오류 나서 주석처리 했습니다 (승하)
from django.contrib.auth.hashers import check_password
from django.http.response import HttpResponse
from .models import CustomUser 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, Change_emailForm
from django.contrib import messages
from django.contrib.auth.views import  PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.shortcuts import resolve_url
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.views.decorators.http import require_POST
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()
INTERNAL_RESET_URL_TOKEN = 'set-password'
INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'

def main(request): 

    return render (request, 'accounts/main2.html')


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
            return redirect('main')



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
    
    def form_valid(self, form):                     #변경하고 message를 이용해서 성공여부를 띄움
        messages.info(self.request, '암호 변경을 완료했습니다.')
        return super().form_valid(form)
    

class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html' 
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    
    def form_valid(self, form):
        if CustomUser.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, 'password_reset_done_fail.html') #email이 존재하지 않을때 
            
class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html' 




class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordForm
    success_url=reverse_lazy('password_reset_complete')
    template_name = 'accounts/password_reset_confirm.html'

    def form_valid(self, form):
        return super().form_valid(form)

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = resolve_url(settings.LOGIN_URL)
        return context


def User_delete(request):
    if request.method == "POST":
        pw_del = request.POST["pw_del"]
        user = request.user
        if check_password(pw_del, user.password):
            user.delete()
            return redirect('main')


    return render (request, 'accounts/user_delete.html')

