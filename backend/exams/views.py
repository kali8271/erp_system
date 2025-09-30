from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Exam
from .forms import ExamForm

# -----------------------------
# Template-based Views (Frontend)
# -----------------------------

@login_required
def exam_list(request):
    # Fetch all exams along with their related section/course
    exams = Exam.objects.select_related("section", "section__course").all()
    return render(request, "exams/exam_list.html", {"object_list": exams})

@login_required
def exam_detail(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    return render(request, "exams/exam_detail.html", {"object": exam})

@login_required
def exam_create(request):
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("exams:exam_list")
    else:
        form = ExamForm()
    return render(request, "exams/exam_form.html", {"form": form})

@login_required
def exam_update(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == "POST":
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect("exams:exam_list")
    else:
        form = ExamForm(instance=exam)
    return render(request, "exams/exam_form.html", {"form": form, "object": exam})

@login_required
def exam_delete(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == "POST":
        exam.delete()
        return redirect("exams:exam_list")
    return render(request, "exams/exam_confirm_delete.html", {"object": exam})


# -----------------------------
# API Views (commented out)
# -----------------------------
"""
from rest_framework import viewsets, permissions
from .serializers import ExamSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.select_related("section", "section__course")
    serializer_class = ExamSerializer
    permission_classes = [permissions.IsAuthenticated]
"""
