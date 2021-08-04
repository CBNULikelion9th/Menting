from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser) #커스텀 튜저 정보를 어드민 페이지에서 보기 위함
