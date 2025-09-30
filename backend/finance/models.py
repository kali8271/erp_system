from django.db import models
from django.utils import timezone


class Fee(models.Model):
    student = models.ForeignKey("accounts.StudentProfile", on_delete=models.CASCADE, related_name="fees")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    description = models.CharField(max_length=200, blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fee for {self.student.user.username} - {self.amount} (Paid: {self.is_paid})"


class Payment(models.Model):
    student = models.ForeignKey("accounts.StudentProfile", on_delete=models.CASCADE, related_name="payments")
    fee = models.ForeignKey(Fee, on_delete=models.SET_NULL, null=True, blank=True, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=timezone.now)
    method = models.CharField(
        max_length=20,
        choices=[
            ("cash", "Cash"),
            ("card", "Card"),
            ("bank_transfer", "Bank Transfer"),
            ("online", "Online"),
        ],
        default="cash",
    )
    reference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Payment {self.amount} by {self.student.user.username}"


class Scholarship(models.Model):
    student = models.ForeignKey("accounts.StudentProfile", on_delete=models.CASCADE, related_name="scholarships")
    name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    awarded_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.student.user.username} ({self.amount})"


class Fine(models.Model):
    student = models.ForeignKey("accounts.StudentProfile", on_delete=models.CASCADE, related_name="fines")
    reason = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_date = models.DateField(default=timezone.now)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Fine {self.amount} - {self.student.user.username} ({self.reason})"
