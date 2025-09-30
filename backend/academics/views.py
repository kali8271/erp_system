from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Department, Course, Section

# ----------------- API Views (commented out) -----------------
# from rest_framework import viewsets, permissions
# from .serializers import DepartmentSerializer, CourseSerializer, SectionSerializer
#
# class DepartmentViewSet(viewsets.ModelViewSet):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
# class CourseViewSet(viewsets.ModelViewSet):
#     queryset = Course.objects.select_related("department")
#     serializer_class = CourseSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
# class SectionViewSet(viewsets.ModelViewSet):
#     queryset = Section.objects.select_related("course", "teacher")
#     serializer_class = SectionSerializer
#     permission_classes = [permissions.IsAuthenticated]

# ----------------- Department Views -----------------
class DepartmentListView(ListView):
    model = Department
    template_name = "academics/department_list.html"
    context_object_name = "departments"

class DepartmentDetailView(DetailView):
    model = Department
    template_name = "academics/department_detail.html"
    context_object_name = "department"

class DepartmentCreateView(CreateView):
    model = Department
    fields = ["code", "name"]
    template_name = "academics/department_form.html"
    success_url = reverse_lazy("academics:department_list")

class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ["code", "name"]
    template_name = "academics/department_form.html"
    success_url = reverse_lazy("academics:department_list")

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = "academics/department_confirm_delete.html"
    success_url = reverse_lazy("academics:department_list")

# ----------------- Course Views -----------------
class CourseListView(ListView):
    model = Course
    template_name = "academics/course_list.html"
    context_object_name = "courses"

class CourseDetailView(DetailView):
    model = Course
    template_name = "academics/course_detail.html"
    context_object_name = "course"

class CourseCreateView(CreateView):
    model = Course
    fields = ["code", "title", "credits", "department"]
    template_name = "academics/course_form.html"
    success_url = reverse_lazy("academics:course_list")

class CourseUpdateView(UpdateView):
    model = Course
    fields = ["code", "title", "credits", "department"]
    template_name = "academics/course_form.html"
    success_url = reverse_lazy("academics:course_list")

class CourseDeleteView(DeleteView):
    model = Course
    template_name = "academics/course_confirm_delete.html"
    success_url = reverse_lazy("academics:course_list")

# ----------------- Section Views -----------------
class SectionListView(ListView):
    model = Section
    template_name = "academics/section_list.html"
    context_object_name = "sections"

class SectionDetailView(DetailView):
    model = Section
    template_name = "academics/section_detail.html"
    context_object_name = "section"

class SectionCreateView(CreateView):
    model = Section
    fields = ["course", "section_code", "teacher", "semester"]
    template_name = "academics/section_form.html"
    success_url = reverse_lazy("academics:section_list")

class SectionUpdateView(UpdateView):
    model = Section
    fields = ["course", "section_code", "teacher", "semester"]
    template_name = "academics/section_form.html"
    success_url = reverse_lazy("academics:section_list")

class SectionDeleteView(DeleteView):
    model = Section
    template_name = "academics/section_confirm_delete.html"
    success_url = reverse_lazy("academics:section_list")
