from django.shortcuts import render, redirect
from .forms import Mentee_requestForm
from .models import Mentee_request


def request_view(request):
    if request.method == 'GET':
        form = Mentee_requestForm()
        

    elif request.method == 'POST':
        form = Mentee_requestForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect ('requestslist')

    return render (request, 'menteerequest/requestform.html',{'form':form})


def requests_list(request):
    request_list = Mentee_request.objects.all() #이부분은 get또는 filter 로 바꾸어 리스트를 걸러 내야한다
    return render (request, 'menteerequest/requestlist.html',{'request_list':request_list})