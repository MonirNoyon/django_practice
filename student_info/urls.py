from django.contrib import admin
from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('insert/', views.insertData),
    path('view/', views.viewData),
    path('update/<int:pk>/', views.updateData),
    path('custom-update/', views.customUpdate),
    path('delete/', views.deleteData),
    path('login/', views.user_login),
    path('token_check/', views.user_token_check),
    path('stu_login/', views.student_login),
    path('usr_registration/', views.user_registration),
    path('logout/', knox_views.LogoutView.as_view()),
]