from django.urls import path
from . import views

urlpatterns = [
    path('community/',views.community_page, name='community_page'),
    path('notice/',views.notice_page, name='notice_page'),
    path('search/',views.search_page, name='search_page'),
]