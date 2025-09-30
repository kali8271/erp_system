from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Notice
from .forms import NoticeForm

@login_required
def notice_list(request):
    notices = Notice.objects.select_related("created_by").all()
    return render(request, "notices/notice_list.html", {"object_list": notices})

@login_required
def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, "notices/notice_detail.html", {"object": notice})

@login_required
def notice_create(request):
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.created_by = request.user
            notice.save()
            return redirect("notices:notice_list")
    else:
        form = NoticeForm()
    return render(request, "notices/notice_form.html", {"form": form})

@login_required
def notice_update(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect("notices:notice_list")
    else:
        form = NoticeForm(instance=notice)
    return render(request, "notices/notice_form.html", {"form": form, "object": notice})

@login_required
def notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        notice.delete()
        return redirect("notices:notice_list")
    return render(request, "notices/notice_confirm_delete.html", {"object": notice})

# -----------------------------
# API code commented out
# -----------------------------
"""
from rest_framework import viewsets, permissions
from .serializers import NoticeSerializer

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.select_related("created_by")
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAuthenticated]
"""
