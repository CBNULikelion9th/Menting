#from Menting.accounts.models import CustomUser 오류 나서 주석처리 했습니다 (승하)
from .models import CustomUser  
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages


def main(request):   
    u_uni = CustomUser.university
    
    print(u_uni)
    lis = [u_uni]
  # customer_list = CustomUser.objects.filter(university = request.POST.get('keyword'''))
   # a=[]#
   # a.append(customer_list)#
   # print(a)#
    #if a == None:#
        #print('오류')
        #return render(request, 'accounts/main.html', {'lis':lis} )
  #  else  #
    return render(request, 'accounts/main.html')
 
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
            messages.add_message(request, messages.INFO, '아이디와 비밀번호를 확인하세요!')
            return redirect('login')
        
                


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



        else:
            messages.add_message(request, messages.INFO, '회원 가입에 실패 했습니다.')
            return redirect('signup')



    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form':form})



def home(request):
    return render(request, 'accounts/home.html')


def success(request):
    return render(request, 'accounts/success.html')

def mypage(request):
    return render(request, 'accounts/mypage.html')

    

