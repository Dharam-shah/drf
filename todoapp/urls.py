from django import views
from django.urls import path,include
from todoapp import views
from rest_framework.routers import DefaultRouter

#creating router object
router = DefaultRouter()
#register TodoAppCRUD with router
router.register('todoapi', views.TodoAppCRUD, basename='todoapi')

urlpatterns = [
    #path("", test, name="test"),
    path('', include(router.urls)),
    #path("todoapilc/", TodoAppLC.as_view(), name="todoapilc"),
]