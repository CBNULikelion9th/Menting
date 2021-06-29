from django.urls import path
from . import views

urlpatterns = [
    path('list/request', views.request_view, name = 'requestform'),
    path('list/request_list', views.requests_list, name = 'requestslist'),
]