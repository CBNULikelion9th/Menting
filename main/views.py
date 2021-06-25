from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm
from .models import Post

def community_page(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
    }

    return render(request, 'main/community_page.html', context)

def community_new(request):
    if request.method == 'GET':
        form = PostForm()

    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('community_detail', post_id=post.id)

    return render(request, 'main/community_new.html',{
        'form': form,
    })

def community_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
    }

    return render(request, 'main/community_detail.html',context)

def notice_page(request):
    return render(request, 'main/notice_page.html')

def search_page(request):
    return render(request, 'main/search_page.html')
