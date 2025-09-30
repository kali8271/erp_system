from django.urls import path
from . import views

app_name = "notices"

urlpatterns = [
    path("", views.notice_list, name="notice_list"),
    path("add/", views.notice_create, name="notice_add"),
    path("<int:pk>/", views.notice_detail, name="notice_detail"),
    path("<int:pk>/edit/", views.notice_update, name="notice_edit"),
    path("<int:pk>/delete/", views.notice_delete, name="notice_delete"),

    # API route commented out
    # from rest_framework.routers import DefaultRouter
    # router = DefaultRouter()
    # router.register("notices", views.NoticeViewSet, basename="notices")
]
