from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Timetable
from .forms import TimetableForm

@login_required
def timetable_list(request):
    items = Timetable.objects.select_related("course", "section").all()
    return render(request, "timetable/timetable_list.html", {"object_list": items})

@login_required
def timetable_detail(request, pk):
    item = get_object_or_404(Timetable, pk=pk)
    return render(request, "timetable/timetable_detail.html", {"object": item})

@login_required
def timetable_create(request):
    if request.method == "POST":
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("timetable:timetable_list")
    else:
        form = TimetableForm()
    return render(request, "timetable/timetable_form.html", {"form": form})

@login_required
def timetable_update(request, pk):
    item = get_object_or_404(Timetable, pk=pk)
    if request.method == "POST":
        form = TimetableForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("timetable:timetable_list")
    else:
        form = TimetableForm(instance=item)
    return render(request, "timetable/timetable_form.html", {"form": form, "object": item})

@login_required
def timetable_delete(request, pk):
    item = get_object_or_404(Timetable, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("timetable:timetable_list")
    return render(request, "timetable/timetable_confirm_delete.html", {"object": item})

# -----------------------------
# API code commented out
# -----------------------------
"""
from rest_framework import viewsets, permissions
from .serializers import TimetableSerializer

class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.select_related("course", "section")
    serializer_class = TimetableSerializer
    permission_classes = [permissions.IsAuthenticated]
"""
