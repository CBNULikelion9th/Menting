from django.shortcuts import render

def community_page(request):
    return render(request, 'main/community_page.html')

def notice_page(request):
    return render(request, 'main/notice_page.html')

def search_page(request):
    return render(request, 'main/search_page.html')
