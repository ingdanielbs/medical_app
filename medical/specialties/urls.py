from . import views
from django.urls import path

urlpatterns = [
    path("", views.specialties, name="specialties"),
    path("edit/<int:id>", views.edit_specialty, name="edit_specialty"),
    path("delete/<int:id>", views.delete_specialty, name="delete_specialty"),
]