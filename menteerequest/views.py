from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Mentee_requestForm, ResponseForm ,PointForm
from .models import Mentee_request, Mname, Response #평점에 조건 username을 얻기위해 만든 모델
from accounts.models import CustomUser
from main.models import Mentor #멘토 선택에서 선택한 정보를 가저오기 위한 모델
from django.core.mail import EmailMessage
from django.conf import settings



def request_view(request):
    # for e in request.__dict__:
    #     print(e)
    if request.method == 'GET':
        form = Mentee_requestForm()
        

    elif request.method == 'POST':
        form = Mentee_requestForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False) 
            post.mentor = Mentor.username   #폼에 추가적으로 저장할 멘토의 아이디와 이메일 이부분은 metor모델에 저장된 값을 가져와서 이 폼에 저장한다
            post.mentor_email = Mentor.email
            post.mentee = request.user
            post.save()
            return redirect ('requestsuccess')

    return render (request, 'menteerequest/requestform.html',{'form':form})


def requests_list(request):
    #멘티에게 보여지는 리스트
    if request.user.studenttype == False:
        request_list = Mentee_request.objects.filter( mentee = request.user) 
        return render (request, 'menteerequest/mentee_request_list.html',{'request_list':request_list})

    else:#멘토에게 들어온 요청을 보여줌
        request_list = Mentee_request.objects.filter( mentor = request.user) 
        return render (request, 'menteerequest/mentor_request_list.html',{'request_list':request_list})


def success_request_view(request): # 요청을 성공적으로 작성하면 멘토의 유저정보에 있는 이메일에 메일이 보내진다
    email = EmailMessage(
        'Menting의 요청이 들어왔습니다',                # 제목
        'Menting에서 당신에게 필요한 요청이 들어왔습니다 홈페이지에 접속해서 확인헤 주세요. http://127.0.0.1:8000',       # 내용
        to=[Mentor.email],  #  멘토 모델 사용받는 이메일 리스트
        )
    email.send()
    return redirect ('requestslist')

#   기서 Mentor의 값에는 (1) (2) ....반복 할 수록 많이 들어가게 되는데 어떻게 마지막으로 저장된 부분을 가져오는 걸까 다른 부분에 사용하면 여러개의 값을 가지고 있어 특정해 줘야한다 아니면 오류가 나옴 



def request_detail(request,post_id):  # 디테일 페이지
    
    post = Mentee_request.objects.get(id = post_id) #선택한 post를 가져온다
    Mname.username = post.mentor  # 그 포스트에 저장된 mentor를 새로운 모델에 저장
    Mname.post_id = post.id 
    return render (request, 'menteerequest/request_detail.html',{'post':post})


def request_response(request, post_id):
    post = get_object_or_404(Mentee_request, id=post_id) 
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user  #응답에 작성자 멘토아이디
            response.post = post
            response.save()
            return redirect('requestdetail', post_id=post.id)
    else:
        form = ResponseForm()
    return render(request, 'menteerequest/request_response.html', {'form': form})


def request_response_reject(request, post_id):
    post = get_object_or_404(Mentee_request, id=post_id) 
    
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            post.finish_check = 1
            post.save()
            response = form.save(commit=False)
            response.author = request.user
            response.text = '거절 되었습니다 ㅠ'
            response.post = post
            response.save()
            return redirect('requestdetail', post_id=post.id)
    else:
        form = ResponseForm()
    return render(request, 'menteerequest/request_response_reject.html', {'form': form})



def grade_point(request):  #평점 계산
    userr = CustomUser.objects.get(username = Mname.username) #커스텀 우유져 폼에 평점을 넣기 위해 가져옴
    k = get_object_or_404(Mentee_request, id=Mname.post_id) #멘토리스트를 가져와 완료를 체크 하기 위함

    if request.method == 'POST':
        form = PointForm(request.POST)
        if form.is_valid():
            k.finish_check = 1  #멘팅 완료 체크
            k.save()
            post = form.save(commit = False)
            userr.grade = int(post.grade) + userr.grade
            userr.count = userr.count + 1
            userr.avg = userr.grade / userr.count
            userr.save()
            return render (request, 'menteerequest/grade_success.html')
        
        return HttpResponse('fail')

    else:
        form = PointForm()

    return render (request, 'menteerequest/grade.html',{'form':form})

