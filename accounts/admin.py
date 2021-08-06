from django.contrib import admin
from .models import CustomUser,University

admin.site.register(CustomUser) #커스텀 튜저 정보를 어드민 페이지에서 보기 위함
admin.site.register(University) #첫 페이지 검색에 들어가는 대학교 이름 모델