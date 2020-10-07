
from django.contrib import admin
from django.urls import path

import cloudservice.views


# url경로 정의
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cloudservice.views.view), # http://127.0.0.1:8000와 views.py의 view함수 연결
    path('sends/', cloudservice.views.send, name='sendurl') #http://127.0.0.1:8000/sends와 views.py의 send함수 연결 
]
