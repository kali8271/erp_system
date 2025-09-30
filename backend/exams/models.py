from django.db import models


class Exam(models.Model):
    section = models.ForeignKey("academics.Section", on_delete=models.CASCADE, related_name="exams")
    title = models.CharField(max_length=200)   # e.g., Midterm, Final, Quiz
    date = models.DateField()
    max_marks = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.title} - {self.section} ({self.date})"


class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="results")
    student = models.ForeignKey("accounts.StudentProfile", on_delete=models.CASCADE, related_name="results")
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2, blank=True)

    class Meta:
        unique_together = ("exam", "student")

    def __str__(self):
        return f"{self.student.user.username} - {self.exam.title}: {self.marks_obtained}"

    def save(self, *args, **kwargs):
        # auto-grade calculation
        if self.marks_obtained is not None and self.exam.max_marks > 0:
            percentage = (self.marks_obtained / self.exam.max_marks) * 100
            if percentage >= 90:
                self.grade = "A+"
            elif percentage >= 80:
                self.grade = "A"
            elif percentage >= 70:
                self.grade = "B"
            elif percentage >= 60:
                self.grade = "C"
            elif percentage >= 50:
                self.grade = "D"
            else:
                self.grade = "F"
        super().save(*args, **kwargs)
