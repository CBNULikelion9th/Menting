from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm, PostForm2, PostForm3
from .models import Post, Comment, Post2

def home(request):
    return render(request, 'main/home.html')

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
    post_form2 = PostForm2()
    context = {
        'post': post,
        'post_form2': post_form2,
    }

    return render(request, 'main/community_detail.html',context)

def community_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()   
    return redirect('community_page')

def community_comment(request, post_id):
    commentt = PostForm2(request.POST)
    if commentt.is_valid():
        commentt = commentt.save(commit=False)
        commentt.post = get_object_or_404(Post, pk=post_id)
        commentt.save()
    return redirect('community_detail', post_id)

def notice_page(request):
    post2_list = Post2.objects.all()
    context = {
        'post2_list': post2_list,
    }
    return render(request, 'main/notice_page.html', context)

def notice_new(request):
    if request.method == 'GET':
        form = PostForm3()

    elif request.method == 'POST':
        form = PostForm3(request.POST)
        if form.is_valid():
            post2 = form.save()
            return redirect('notice_page')

    return render(request, 'main/notice_new.html',{
        'form': form,
    })

def notice_detail(request, post_id):
    post2 = Post2.objects.get(id=post_id)
    post_form2 = PostForm2()
    context = {
        'post2': post2,
        'post_form2': post_form2,
    }

    return render(request, 'main/notice_detail.html',context)

def notice_delete(request, post_id):
    post2 = get_object_or_404(Post2, id=post_id)
    post2.delete()   
    return redirect('notice_page')

def search_page(request):
    return render(request, 'main/search_page.html')
