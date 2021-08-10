from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('top/', views.top_page, name="top_page"),
    path('login/',
         LoginView.as_view(
             template_name='login/index.html'
         ),
         name="login"
         ),
    path('logout/',
         LogoutView.as_view(
             template_name='logout/index.html'
         ),
         name="logout"
         ),

]
