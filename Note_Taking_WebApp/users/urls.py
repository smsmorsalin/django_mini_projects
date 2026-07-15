from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.log_out, name='logout'),
]
