# from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    DepartmentListView, DepartmentDetailView, DepartmentCreateView,
    DepartmentUpdateView, DepartmentDeleteView,
    CourseListView, CourseDetailView, CourseCreateView,
    CourseUpdateView, CourseDeleteView,
    SectionListView, SectionDetailView, SectionCreateView,
    SectionUpdateView, SectionDeleteView,
)

# ----------------- API URLs (commented out) -----------------
# router = DefaultRouter()
# router.register("departments", DepartmentViewSet, basename="departments")
# router.register("courses", CourseViewSet, basename="courses")
# router.register("sections", SectionViewSet, basename="sections")
#
# urlpatterns = [
#     path("", include(router.urls)),
# ]


# ----------------- Template URLs -----------------

app_name = "academics"
urlpatterns = [
    # Department URLs
    path("departments/", DepartmentListView.as_view(), name="department_list"),
    path("departments/<int:pk>/", DepartmentDetailView.as_view(), name="department_detail"),
    path("departments/add/", DepartmentCreateView.as_view(), name="department_add"),
    path("departments/<int:pk>/edit/", DepartmentUpdateView.as_view(), name="department_edit"),
    path("departments/<int:pk>/delete/", DepartmentDeleteView.as_view(), name="department_delete"),

    # Course URLs
    path("courses/", CourseListView.as_view(), name="course_list"),
    path("courses/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path("courses/add/", CourseCreateView.as_view(), name="course_add"),
    path("courses/<int:pk>/edit/", CourseUpdateView.as_view(), name="course_edit"),
    path("courses/<int:pk>/delete/", CourseDeleteView.as_view(), name="course_delete"),

    # Section URLs
    path("sections/", SectionListView.as_view(), name="section_list"),
    path("sections/<int:pk>/", SectionDetailView.as_view(), name="section_detail"),
    path("sections/add/", SectionCreateView.as_view(), name="section_add"),
    path("sections/<int:pk>/edit/", SectionUpdateView.as_view(), name="section_edit"),
    path("sections/<int:pk>/delete/", SectionDeleteView.as_view(), name="section_delete"),
]
