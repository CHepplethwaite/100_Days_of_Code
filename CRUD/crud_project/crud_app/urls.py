from django.urls import path
from . import views as crud_views

urlpatterns = [
    path("",crud_views.ListCBV.as_view(),name="list"),
    path("create/",crud_views.CreateCBV.as_view(),name="create"),
    path("update/",crud_views.UpdateCBV.as_view(),name="update"),
    path("delete/",crud_views.DeleteCBV.as_view(),name="delete"),
    path("<pk>/",crud_views.DetailCBV.as_view(),name="detail"),
]