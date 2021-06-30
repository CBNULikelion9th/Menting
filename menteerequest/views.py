from django.shortcuts import render, redirect, get_object_or_404
from .forms import Mentee_requestForm, ResponseForm
from .models import Mentee_request


def request_view(request):
    # for e in request.__dict__:
    #     print(e)
    if request.method == 'GET':
        form = Mentee_requestForm()
        

    elif request.method == 'POST':
        form = Mentee_requestForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.mentee = request.user
            post.save()
            return redirect ('requestsuccess')

    return render (request, 'menteerequest/requestform.html',{'form':form})


def requests_list(request):
    #멘티에게 보여지는 리스트
    if request.user.studenttype == False:
        request_list = Mentee_request.objects.filter( mentee = request.user) 
        return render (request, 'menteerequest/mentee_request_list.html',{'request_list':request_list})

    else:
        request_list = Mentee_request.objects.filter( mentor = request.user) 
        return render (request, 'menteerequest/mentor_request_list.html',{'request_list':request_list})


def success_request_view(request):

    return render (request, 'menteerequest/success_request.html')

def request_detail(request,post_id):
    
    post = Mentee_request.objects.get(id = post_id)
    return render (request, 'menteerequest/request_detail.html',{'post':post})


def request_response(request, post_id):
    post = get_object_or_404(Mentee_request, id=post_id) #Post를 인자로 받고 get()함수로 넘김? 객체가 존재하지 않으면 오류 발생
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user
            response.post = post
            response.save()
            return redirect('requestdetail', post_id=post.id)
    else:
        form = ResponseForm()
    return render(request, 'menteerequest/request_response.html', {'form': form})


def request_response_reject(request, post_id):
    post = get_object_or_404(Mentee_request, id=post_id) #Post를 인자로 받고 get()함수로 넘김? 객체가 존재하지 않으면 오류 발생
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user
            response.text = '거절 되었습니다 ㅠ'
            response.post = post
            response.save()
            return redirect('requestdetail', post_id=post.id)
    else:
        form = ResponseForm()
    return render(request, 'menteerequest/request_response_reject.html', {'form': form})

