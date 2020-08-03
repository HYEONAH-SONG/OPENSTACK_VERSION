
from django.contrib import admin
from django.urls import path

import cloudservice.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cloudservice.views.view),
    path('sends/', cloudservice.views.send, name='sendurl'),
]
