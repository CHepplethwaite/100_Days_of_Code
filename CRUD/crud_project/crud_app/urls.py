from django.urls import path
from . import views as crud_views

urlpatterns = [
    path("",crud_views.CreateCBV.as_view(),name="create"),
    path("Update/",crud_views.UpdateCBV.as_view,name="update"),
    path("delete/",crud_views.DeleteCBV.as_view,name="delete"),
]
