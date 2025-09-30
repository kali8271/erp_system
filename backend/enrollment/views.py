# from rest_framework import viewsets, permissions
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Enrollment

# ----------------- API Views (commented out) -----------------
# from .serializers import EnrollmentSerializer
#
# class EnrollmentViewSet(viewsets.ModelViewSet):
#     queryset = Enrollment.objects.select_related("student", "section")
#     serializer_class = EnrollmentSerializer
#     permission_classes = [permissions.IsAuthenticated]

# ----------------- Template Views -----------------

class EnrollmentListView(ListView):
    model = Enrollment
    template_name = "enrollment/enrollment_list.html"
    context_object_name = "enrollments"


class EnrollmentDetailView(DetailView):
    model = Enrollment
    template_name = "enrollment/enrollment_detail.html"


class EnrollmentCreateView(CreateView):
    model = Enrollment
    fields = ["student", "section", "status"]
    template_name = "enrollment/enrollment_form.html"
    success_url = reverse_lazy("enrollment_list")


class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    fields = ["student", "section", "status"]
    template_name = "enrollment/enrollment_form.html"
    success_url = reverse_lazy("enrollment_list")


class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = "enrollment/enrollment_confirm_delete.html"
    success_url = reverse_lazy("enrollment_list")
