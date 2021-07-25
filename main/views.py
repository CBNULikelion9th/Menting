from django.forms.fields import CharField
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm, PostForm2, PostForm3, RecommentForm
from .models import Post, Comment, Post2, Mentor, Recomment
from accounts.forms import SignUpForm
from accounts.models import CustomUser, University


def home(request):
    return render(request, 'accounts/main.html')

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
            post.user = request.user
            post.save()
            return redirect('community_page')

    return render(request, 'main/community_new.html',{
        'form': form,
    })

def community_edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'GET':
        form = PostForm(instance=post)

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('community_detail', post_id=post.id)

    return render(request, 'main/community_edit.html',{
        'form': form,
        'post': post,
    })

def community_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    post_form2 = PostForm2()
    recomment_form = RecommentForm()
    context = {
        'post': post,
        'post_form2': post_form2,
        'recomment_form': recomment_form,
    }

    return render(request, 'main/community_detail.html',context)

def community_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()   
    return redirect('community_page')

def community_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    commentt = PostForm2(request.POST)
    if commentt.is_valid():
        commentt = commentt.save(commit=False)
        commentt.post = get_object_or_404(Post, pk=post_id)
        commentt.name = request.user
        commentt.save()
    return redirect('community_detail', post_id=post.id)

def community_recomment(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    recomment = RecommentForm(request.POST)
    if recomment.is_valid():
        recomment = recomment.save(commit=False)
        recomment.comment = get_object_or_404(Comment, pk=comment_id)
        recomment.name2 = request.user
        recomment.save()
    return redirect('community_detail', post_id = post.id)

def comment_delete(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()   
    return redirect('community_detail', post_id = post.id)

def recomment_delete(request, post_id, recomment_id):
    post = get_object_or_404(Post, id=post_id)
    recomment = get_object_or_404(Recomment, id=recomment_id)
    recomment.delete()   
    return redirect('community_detail', post_id = post.id)

def comment_edit(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'GET':
        form = PostForm2(instance=comment)

    elif request.method == 'POST':
        form = PostForm2(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('community_detail', post_id=post.id)

    return render(request, 'main/comment_edit.html',{
        'form': form,
        'comment': comment,
        'post':post,
    })

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


# def univer (request,a_id):
#     t = University.objects.get(a_id =id)
#     return render(request, 'search_page',{'t':t})



def search_page(request,univers):
    # univer2 = University.objects.get(univer = chr(univers))
    customer_list = CustomUser.objects.filter( university = univers )
    
    context = {
        'customer_list': customer_list,
    }

    return render(request, 'main/search_page.html', context)

def search_pages(request):
    
    customer_list = CustomUser.objects.all()
    context = {
        'customer_list': customer_list,
    }

    return render(request, 'main/search_pages.html', context)


def choice_mentor(request,customer_id):
    mentor = CustomUser.objects.get(id =customer_id)
    Mentor.username = mentor.username
    Mentor.email = mentor.email
    return redirect("requestform")