from django.urls import path
from . import views

urlpatterns = [
    path('list/request/', views.request_view, name = 'requestform'),
    path('list/request_list/', views.requests_list, name = 'requestslist'),
    path('list/request_success/', views.success_request_view, name = 'requestsuccess'),
    path('list/request_list/<int:post_id>', views.request_detail, name = 'requestdetail'),
    path('list/request_list/<int:post_id>/response/',views.request_response,name='response'),
    path('list/request_list/<int:post_id>/response_reject/',views.request_response_reject,name='response_reject'),
]