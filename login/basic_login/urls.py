from django.urls import path
from . import views

urlpatterns = [
    path('',views.LoginPage,name='login'),
    path('login/',views.LoginPage, name='login'),
    path('home/',views.HomePage, name='home'),
    path('registration/', views.RegPage, name='register')

]