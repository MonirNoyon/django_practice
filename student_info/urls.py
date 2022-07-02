from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insertData),
    path('view/', views.viewData),
    path('update/<int:pk>/', views.updateData),
    path('custom-update/', views.customUpdate),
    path('delete/', views.deleteData),
    path('login/', views.user_login),
    path('token_check/', views.user_token_check),
]