from django.urls import path,include
from Library_Management_App.api import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('book',views.Book_List_View)

urlpatterns=[
    path('',include(router.urls)),
]