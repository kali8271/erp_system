from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Fee, Payment, Scholarship, Fine
from .forms import FeeForm, PaymentForm, ScholarshipForm, FineForm

# ---------------------- Fee ----------------------
@login_required
def fee_list(request):
    fees = Fee.objects.all()
    return render(request, "finance/fee_list.html", {"object_list": fees})

@login_required
def fee_detail(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    return render(request, "finance/fee_detail.html", {"object": fee})

@login_required
def fee_create(request):
    if request.method == "POST":
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("finance:fee_list")
    else:
        form = FeeForm()
    return render(request, "finance/fee_form.html", {"form": form})

@login_required
def fee_update(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    if request.method == "POST":
        form = FeeForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            return redirect("finance:fee_list")
    else:
        form = FeeForm(instance=fee)
    return render(request, "finance/fee_form.html", {"form": form, "object": fee})

@login_required
def fee_delete(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    if request.method == "POST":
        fee.delete()
        return redirect("finance:fee_list")
    return render(request, "finance/fee_confirm_delete.html", {"object": fee})

# ---------------------- Payment ----------------------
@login_required
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, "finance/payment_list.html", {"object_list": payments})

@login_required
def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, "finance/payment_detail.html", {"object": payment})

@login_required
def payment_create(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("finance:payment_list")
    else:
        form = PaymentForm()
    return render(request, "finance/payment_form.html", {"form": form})

@login_required
def payment_update(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect("finance:payment_list")
    else:
        form = PaymentForm(instance=payment)
    return render(request, "finance/payment_form.html", {"form": form, "object": payment})

@login_required
def payment_delete(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        payment.delete()
        return redirect("finance:payment_list")
    return render(request, "finance/payment_confirm_delete.html", {"object": payment})

# ---------------------- Scholarship ----------------------
@login_required
def scholarship_list(request):
    scholarships = Scholarship.objects.all()
    return render(request, "finance/scholarship_list.html", {"object_list": scholarships})

@login_required
def scholarship_detail(request, pk):
    scholarship = get_object_or_404(Scholarship, pk=pk)
    return render(request, "finance/scholarship_detail.html", {"object": scholarship})

@login_required
def scholarship_create(request):
    if request.method == "POST":
        form = ScholarshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("finance:scholarship_list")
    else:
        form = ScholarshipForm()
    return render(request, "finance/scholarship_form.html", {"form": form})

@login_required
def scholarship_update(request, pk):
    scholarship = get_object_or_404(Scholarship, pk=pk)
    if request.method == "POST":
        form = ScholarshipForm(request.POST, instance=scholarship)
        if form.is_valid():
            form.save()
            return redirect("finance:scholarship_list")
    else:
        form = ScholarshipForm(instance=scholarship)
    return render(request, "finance/scholarship_form.html", {"form": form, "object": scholarship})

@login_required
def scholarship_delete(request, pk):
    scholarship = get_object_or_404(Scholarship, pk=pk)
    if request.method == "POST":
        scholarship.delete()
        return redirect("finance:scholarship_list")
    return render(request, "finance/scholarship_confirm_delete.html", {"object": scholarship})

# ---------------------- Fine ----------------------
@login_required
def fine_list(request):
    fines = Fine.objects.all()
    return render(request, "finance/fine_list.html", {"object_list": fines})

@login_required
def fine_detail(request, pk):
    fine = get_object_or_404(Fine, pk=pk)
    return render(request, "finance/fine_detail.html", {"object": fine})

@login_required
def fine_create(request):
    if request.method == "POST":
        form = FineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("finance:fine_list")
    else:
        form = FineForm()
    return render(request, "finance/fine_form.html", {"form": form})

@login_required
def fine_update(request, pk):
    fine = get_object_or_404(Fine, pk=pk)
    if request.method == "POST":
        form = FineForm(request.POST, instance=fine)
        if form.is_valid():
            form.save()
            return redirect("finance:fine_list")
    else:
        form = FineForm(instance=fine)
    return render(request, "finance/fine_form.html", {"form": form, "object": fine})

@login_required
def fine_delete(request, pk):
    fine = get_object_or_404(Fine, pk=pk)
    if request.method == "POST":
        fine.delete()
        return redirect("finance:fine_list")
    return render(request, "finance/fine_confirm_delete.html", {"object": fine})
