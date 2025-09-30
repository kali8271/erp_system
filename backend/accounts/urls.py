# accounts/urls.py
from django.urls import path
from .views import (
    UserLoginView, UserLogoutView, register_view,
    UserListView,
    UserDetailView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    UserAddView,
    # DRF API views (commented for now)
    # UserViewSet,
    # StudentViewSet,
    # TeacherViewSet,
)

# from rest_framework.routers import DefaultRouter  # Commented out for template-based URLs
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Commented out for now

app_name = "accounts"

# -----------------------------
# Template-based URL patterns
# -----------------------------
urlpatterns = [
    # Authentication
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("user/add/", UserAddView.as_view(), name="user_add"),

    # User CRUD
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/add/", UserAddView.as_view(), name="user_add"),

    path("users/add/", UserCreateView.as_view(), name="user_create"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("users/<int:pk>/edit/", UserUpdateView.as_view(), name="user_update"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
]

# -----------------------------
# DRF API URL patterns (Commented out)
# -----------------------------
# router = DefaultRouter()
# router.register("users", UserViewSet, basename="users")
# router.register("students", StudentViewSet, basename="students")
# router.register("teachers", TeacherViewSet, basename="teachers")
#
# urlpatterns += [
#     path("api/", include(router.urls)),
#     path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
#     path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
# ]
