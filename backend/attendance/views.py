from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance
from .forms import AttendanceForm

# ---------------------------
# Template-based CRUD Views
# ---------------------------

@login_required
def attendance_list(request):
    records = Attendance.objects.select_related("student__user").all()
    return render(request, "attendance/attendance_list.html", {"object_list": records})


@login_required
def attendance_detail(request, pk):
    record = get_object_or_404(Attendance, pk=pk)
    return render(request, "attendance/attendance_detail.html", {"object": record})


@login_required
def attendance_create(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("attendance:attendance_list")
    else:
        form = AttendanceForm()
    return render(request, "attendance/attendance_form.html", {"form": form})


@login_required
def attendance_update(request, pk):
    record = get_object_or_404(Attendance, pk=pk)
    if request.method == "POST":
        form = AttendanceForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("attendance:attendance_list")
    else:
        form = AttendanceForm(instance=record)
    return render(request, "attendance/attendance_form.html", {"form": form, "object": record})


@login_required
def attendance_delete(request, pk):
    record = get_object_or_404(Attendance, pk=pk)
    if request.method == "POST":
        record.delete()
        return redirect("attendance:attendance_list")
    return render(request, "attendance/attendance_confirm_delete.html", {"object": record})

# ---------------------------
# API-based views commented out
# ---------------------------
"""
from rest_framework import viewsets, permissions
from .serializers import AttendanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related("student__user")
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]
"""
