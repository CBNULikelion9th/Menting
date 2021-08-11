from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name = 'login'),
    path('signup/', views.signup_view, name = 'signup'),
    path('logout/', views.logout_view, name = 'logout'),
    path('success/', views.success, name = 'success'),
    path('mypage/', views.mypage, name = 'mypage'),
    path('', views.main, name ='main'),
    path('mypage/change_email/', views.change_email, name = 'change_email'),
    path('mypage/password_change/', views.MyPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done', views.MyPasswordChangeDoneView.as_view(), name = 'password_change_done'),
    path('login/password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('login/password_reset_done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', views.UserPasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("mypage/user_delete/",views.User_delete, name = 'user_delete'),
    
]