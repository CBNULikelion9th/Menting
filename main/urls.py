from django.urls import path
from . import views

urlpatterns = [
    path('community/',views.community_page, name='community_page'),
    path('community/new/',views.community_new, name='community_new'),
    path('community/<int:post_id>/',views.community_detail, name="community_detail"),
    path('notice/',views.notice_page, name='notice_page'),
    path('search/',views.search_page, name='search_page'),
]