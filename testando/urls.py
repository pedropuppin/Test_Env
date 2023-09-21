from django.contrib import admin
from django.urls import path
from testando.views import index

app_name = 'teste'

urlpatterns = [
    path('', index, name='index'),
]