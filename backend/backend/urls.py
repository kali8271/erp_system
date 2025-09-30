from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home and dashboard templates
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("dashboard/", TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),

    # Template-based app URLs
    path("accounts/", include("accounts.urls")),  # login, logout, user CRUD
    path("academics/", include("academics.urls")),  # if you have template-based views
    path("enrollment/", include("enrollment.urls")),
    path("attendance/", include("attendance.urls")),
    path("exams/", include("exams.urls")),
    path("timetable/", include("timetable.urls")),
    path("notices/", include("notices.urls")),
    path("finance/", include("finance.urls")),

    # API routes (prefix with api/)
    # path("api/accounts/", include("accounts.api_urls")),  # if API URLs are split
    # path("api/academics/", include("academics.api_urls")),
    # path("api/enrollment/", include("enrollment.api_urls")),
    # path("api/attendance/", include("attendance.api_urls")),
    # path("api/exams/", include("exams.api_urls")),
    # path("api/timetable/", include("timetable.api_urls")),
    # path("api/notices/", include("notices.api_urls")),
    # path("api/finance/", include("finance.api_urls")),
]
