from . import views
from django.urls import path

urlpatterns = [
    path("", views.specialties, name="specialties")
]