from django.urls import path
from . import views as crud_views

urlpatterns = [
    path("",crud_views.CreateCBV.as_view(),name="create"),
]
