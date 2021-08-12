from django.urls import path
from . import views

urlpatterns = [
    path('community/',views.community_page, name='community_page'),
    path('community/new/',views.community_new, name='community_new'),
    path('community/<int:post_id>/',views.community_detail, name="community_detail"),
    path('community/<int:post_id>/delete/',views.community_delete, name="community_delete"),
    path('community/<int:post_id>/comment/',views.community_comment, name="community_comment"),
    path('community/<int:post_id>/recomment/<int:comment_id>/',views.community_recomment, name="community_recomment"),
    path('community/<int:post_id>/recomment/<int:recomment_id>/delete/',views.recomment_delete, name="recomment_delete"),
    path('community/<int:post_id>/comment/<int:comment_id>/delete/',views.comment_delete, name="comment_delete"),
    path('community/<int:post_id>/comment/<int:comment_id>/edit/',views.comment_edit, name="comment_edit"),
    path('community/<int:post_id>/edit/',views.community_edit, name="community_edit"),
    path('notice/',views.notice_page, name='notice_page'),
    path('notice/new/',views.notice_new, name='notice_new'),
    path('notice/<int:post_id>/',views.notice_detail, name="notice_detail"),
    path('notice/<int:post_id>/delete/',views.notice_delete, name="notice_delete"),
    path('search/<str:univers>/',views.search_page, name='search_page'),
    path('search/',views.search_pages, name='search_pages'),
    path('',views.home, name='home'),
    path('search/choice_mentor/<int:customer_id>',views.choice_mentor, name='choice_mentor'),
    path('cat1/',views.cat_1, name='cat_1'),
    path('cat2/',views.cat_2, name='cat_2'),
    path('cat3/',views.cat_3, name='cat_3'),
]