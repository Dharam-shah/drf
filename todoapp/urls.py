from django.urls import path
from .views import test, TodoAppLC,TodoAppRUD

urlpatterns = [
    path("", test, name="test"),
    path("todoapilc/", TodoAppLC.as_view(), name="todoapilc"),
    path("todoapirud/<int:pk>", TodoAppRUD.as_view(), name="todoapirud"),
]