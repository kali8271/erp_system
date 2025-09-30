from django.urls import path
from . import views

app_name = "exams"

urlpatterns = [
    # Template-based CRUD views
    path("", views.exam_list, name="exam_list"),          # List all exams
    path("add/", views.exam_create, name="exam_add"),    # Create a new exam
    path("<int:pk>/", views.exam_detail, name="exam_detail"),  # Exam details
    path("<int:pk>/edit/", views.exam_update, name="exam_edit"),  # Update exam
    path("<int:pk>/delete/", views.exam_delete, name="exam_delete"),  # Delete exam

    # -----------------------------
    # API routes (commented out)
    # -----------------------------
    # from rest_framework.routers import DefaultRouter
    # router = DefaultRouter()
    # router.register("exams", views.ExamViewSet, basename="exams")
]
