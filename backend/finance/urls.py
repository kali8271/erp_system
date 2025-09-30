from django.urls import path
from . import views

app_name = "finance"

urlpatterns = [
    # Fee
    path("fees/", views.fee_list, name="fee_list"),
    path("fees/add/", views.fee_create, name="fee_add"),
    path("fees/<int:pk>/", views.fee_detail, name="fee_detail"),
    path("fees/<int:pk>/edit/", views.fee_update, name="fee_edit"),
    path("fees/<int:pk>/delete/", views.fee_delete, name="fee_delete"),

    # Payment
    path("payments/", views.payment_list, name="payment_list"),
    path("payments/add/", views.payment_create, name="payment_add"),
    path("payments/<int:pk>/", views.payment_detail, name="payment_detail"),
    path("payments/<int:pk>/edit/", views.payment_update, name="payment_edit"),
    path("payments/<int:pk>/delete/", views.payment_delete, name="payment_delete"),

    # Scholarship
    path("scholarships/", views.scholarship_list, name="scholarship_list"),
    path("scholarships/add/", views.scholarship_create, name="scholarship_add"),
    path("scholarships/<int:pk>/", views.scholarship_detail, name="scholarship_detail"),
    path("scholarships/<int:pk>/edit/", views.scholarship_update, name="scholarship_edit"),
    path("scholarships/<int:pk>/delete/", views.scholarship_delete, name="scholarship_delete"),

    # Fine
    path("fines/", views.fine_list, name="fine_list"),
    path("fines/add/", views.fine_create, name="fine_add"),
    path("fines/<int:pk>/", views.fine_detail, name="fine_detail"),
    path("fines/<int:pk>/edit/", views.fine_update, name="fine_edit"),
    path("fines/<int:pk>/delete/", views.fine_delete, name="fine_delete"),
]
