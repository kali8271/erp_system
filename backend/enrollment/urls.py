# from rest_framework.routers import DefaultRouter
from django.urls import path
# from .views import EnrollmentViewSet
from .views import (
    EnrollmentListView, EnrollmentDetailView, EnrollmentCreateView,
    EnrollmentUpdateView, EnrollmentDeleteView
)

# ----------------- API URLs (commented out) -----------------
# router = DefaultRouter()
# router.register("enrollments", EnrollmentViewSet, basename="enrollments")
# urlpatterns = [
#     path("", include(router.urls)),
# ]

# ----------------- Template URLs -----------------
urlpatterns = [
    path("", EnrollmentListView.as_view(), name="enrollment_list"),
    path("<int:pk>/", EnrollmentDetailView.as_view(), name="enrollment_detail"),
    path("add/", EnrollmentCreateView.as_view(), name="enrollment_add"),
    path("<int:pk>/edit/", EnrollmentUpdateView.as_view(), name="enrollment_edit"),
    path("<int:pk>/delete/", EnrollmentDeleteView.as_view(), name="enrollment_delete"),
]
