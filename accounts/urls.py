from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name = 'login'),
    path('signup/', views.signup_view, name = 'signup'),
    path('logout/', views.logout_view, name = 'logout'),
    path('success/', views.success, name = 'success'),
    path('mypage/', views.mypage, name = 'mypage'),
    path('', views.main, name ='main'),
]