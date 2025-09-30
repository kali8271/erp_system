from django.urls import path
from . import views

app_name = "timetable"

urlpatterns = [
    path("", views.timetable_list, name="timetable_list"),
    path("add/", views.timetable_create, name="timetable_add"),
    path("<int:pk>/", views.timetable_detail, name="timetable_detail"),
    path("<int:pk>/edit/", views.timetable_update, name="timetable_edit"),
    path("<int:pk>/delete/", views.timetable_delete, name="timetable_delete"),

    # API route commented out
    # from rest_framework.routers import DefaultRouter
    # router = DefaultRouter()
    # router.register("timetable", views.TimetableViewSet, basename="timetable")
]
