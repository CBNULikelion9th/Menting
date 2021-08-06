from django.forms.fields import CharField
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from .forms import PostForm, PostForm2, PostForm3, RecommentForm
from .models import Post, Comment, Post2, Mentor, Recomment
from accounts.forms import SignUpForm
from accounts.models import CustomUser, University
from django.contrib import messages




def home(request):
    return render(request, 'accounts/main.html')

def community_page(request):

    post_list = Post.objects.all().order_by('-created_at')


    page = request.GET.get('page', '1')      #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(post_list, 5)      #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.get_page(page)      #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    context = {
        'post_list': page_obj,
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

    post2_list = Post2.objects.all().order_by('-created_at')


    page = request.GET.get('page', '1')      #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(post2_list, 5)      #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.get_page(page)      #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    context = {
        'post2_list': page_obj,
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
<<<<<<< HEAD
    
=======
>>>>>>> 568aa6b3d58a9247dfb4bf29fe73d78339ebc21f
    context = {
        'customer_list': customer_list,
    }

    return render(request, 'main/search_page.html', context)

def search_pages(request):

    customer_list = CustomUser.objects.filter( mentor_check = True)  #멘토체크받은 리스트만 가져옴

    search_type = request.GET.get('search_type','')       #검색 타입 받음
    search_keyword = request.GET.get('search_keyword','')  #검색 키워드 받음

    if search_keyword :   #검색 키워드가 있을 경우
        if len(search_keyword) > 1 :
            if search_type == '아이디':
                customer_list = customer_list.filter(username__icontains = search_keyword)
            elif search_type == '학교':
                customer_list = customer_list.filter(university__icontains = search_keyword)
            elif search_type == '학과':
                customer_list = customer_list.filter(major__icontains = search_keyword)
            elif search_type == '학번':
                customer_list = customer_list.filter(studentnumber__icontains = search_keyword)    
            elif search_type == '입시전형':

                customer_list = customer_list.filter(entrancetype__icontains = search_keyword)
        
        else :     #검색 키워드가 한글자인 경우
            messages.warning(request, "검색어는 2글자 이상 입력해주세요.")


    page = request.GET.get('page', '1')          #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(customer_list, 5)      #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.get_page(page)          #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    page_count = paginator.count                 #게시글 수를 page_count에 저장

    context = {
        'search_keyword': search_keyword,
        'customer_list': page_obj,
        'page_count': page_count,              
        'search_type' : search_type,
    }

    return render(request, 'main/search_pages.html', context)


def choice_mentor(request,customer_id): # 멘토들중 선택     
    mentor = CustomUser.objects.get(id =customer_id)    #선택한 id를 통해서 유저 정보를 가져온다
    Mentor.username = mentor.username   #가져온 유저 정보에서 정보를 requestform에 전달하기 위해 새로운 모델에 정보를 넣는다
    Mentor.email = mentor.email #이멜일 정보를 가져옴
    return redirect("requestform") #요청서 페이지로 넘어간다

