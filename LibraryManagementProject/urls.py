"""LibraryManagementProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Library_Management_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view,name='home'),
    path('allbooks/', views.book_view,name='allbooks'),
    path('createbooks/', views.create_book_view,name='createbooks'),
    path('updatebooks/<pk>', views.update_book_view,name='updatebooks'),
    path('deletebooks/<pk>', views.delete_book_view,name='deletebooks'),


    path('register/', views.register_page_view,name='register'),
    path('login/', views.login_page_view,name='login'),
    path('logout/', views.logout_page_view,name='logout'),

    #for api accessing purpose
    path('api/',include('Library_Management_App.api.urls'))


]
