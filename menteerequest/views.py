from django.shortcuts import render, redirect
from .forms import Mentee_requestForm
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
            return redirect ('requestslist')

    return render (request, 'menteerequest/requestform.html',{'form':form})


def requests_list(request):
    #멘티에게 보여지는 리스트
    if request.user.studenttype == False:
        request_list = Mentee_request.objects.filter( mentee = request.user) 
        return render (request, 'menteerequest/requestlist.html',{'request_list':request_list})

    else:
        request_list = Mentee_request.objects.filter( mentor = request.user) 
        return render (request, 'menteerequest/requestlist.html',{'request_list':request_list})