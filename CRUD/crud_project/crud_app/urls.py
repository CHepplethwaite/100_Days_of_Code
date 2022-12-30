from django.urls import path
from . import views as crud_views

urlpatterns = [
    path("",crud_views.index,name="index"),
]
