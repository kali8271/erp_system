from django.db import models


class Attendance(models.Model):
    section = models.ForeignKey("academics.Section", on_delete=models.CASCADE, related_name="attendances")
    student = models.ForeignKey("accounts.StudentProfile", on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[
            ("present", "Present"),
            ("absent", "Absent"),
            ("late", "Late"),
            ("excused", "Excused"),
        ],
        default="present",
    )
    marked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("section", "student", "date")
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date} | {self.section} | {self.student.user.username} - {self.status}"
