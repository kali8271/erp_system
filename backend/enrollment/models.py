from django.db import models


class Enrollment(models.Model):
    student = models.ForeignKey("accounts.StudentProfile", on_delete=models.CASCADE, related_name="enrollments")
    section = models.ForeignKey("academics.Section", on_delete=models.CASCADE, related_name="enrollments")
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("enrolled", "Enrolled"),
            ("dropped", "Dropped"),
            ("completed", "Completed"),
        ],
        default="enrolled",
    )

    class Meta:
        unique_together = ("student", "section")

    def __str__(self):
        return f"{self.student.user.username} → {self.section}"
