# accounts/views.py

from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm

# DRF imports (commented out for now)
# from rest_framework import viewsets, permissions
# from .serializers import (
#     StudentProfileSerializer,
#     TeacherProfileSerializer,
#     UserSerializer,
# )
# from .models import StudentProfile, TeacherProfile, User

User = get_user_model()


# -----------------------------
# Template-based Views
# -----------------------------

class UserLoginView(LoginView):
    template_name = "accounts/login.html"

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")

class UserAddView(LoginRequiredMixin, FormView):
    template_name = "accounts/user_form.html"  # fallback, mostly unused with popup
    form_class = UserCreationForm
    success_url = reverse_lazy("dashboard")  # redirect after signup

    def form_valid(self, form):
        # Create user
        user = form.save()
        # Optionally log the new user in automatically
        # login(self.request, user)
        return super().form_valid(form)

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in immediately
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})
class UserListView(ListView):
    model = User
    template_name = "accounts/user_list.html"
    context_object_name = "object_list"
    paginate_by = 20


class UserDetailView(DetailView):
    model = User
    template_name = "accounts/user_detail.html"
    context_object_name = "object"


class UserCreateView(CreateView):
    model = User
    template_name = "accounts/user_form.html"
    fields = ["username", "email", "first_name", "last_name", "is_staff", "is_active"]
    success_url = reverse_lazy("accounts:user_list")


class UserUpdateView(UpdateView):
    model = User
    template_name = "accounts/user_form.html"
    fields = ["username", "email", "first_name", "last_name", "is_staff", "is_active"]
    success_url = reverse_lazy("accounts:user_list")


class UserDeleteView(DeleteView):
    model = User
    template_name = "accounts/user_confirm_delete.html"
    success_url = reverse_lazy("accounts:user_list")


# -----------------------------
# DRF API Views (commented out)
# -----------------------------
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAdminUser]
#
#
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = StudentProfile.objects.select_related("user")
#     serializer_class = StudentProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class TeacherViewSet(viewsets.ModelViewSet):
#     queryset = TeacherProfile.objects.select_related("user")
#     serializer_class = TeacherProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
