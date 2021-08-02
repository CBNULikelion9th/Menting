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
    path('password_change/', views.MyPasswordChangeView.as_view(), name='password_change'),
]