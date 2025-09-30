from django import forms
from .models import Fee, Payment, Scholarship, Fine

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ["student", "amount", "due_date", "description", "is_paid"]
        widgets = {"due_date": forms.DateInput(attrs={"type": "date"})}

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["student", "fee", "amount", "payment_date", "method", "reference"]
        widgets = {"payment_date": forms.DateTimeInput(attrs={"type": "datetime-local"})}

class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ["student", "name", "amount", "awarded_date"]
        widgets = {"awarded_date": forms.DateInput(attrs={"type": "date"})}

class FineForm(forms.ModelForm):
    class Meta:
        model = Fine
        fields = ["student", "reason", "amount", "issued_date", "is_paid"]
        widgets = {"issued_date": forms.DateInput(attrs={"type": "date"})}
