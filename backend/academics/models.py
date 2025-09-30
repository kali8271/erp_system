from django.db import models


class Department(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    credits = models.DecimalField(max_digits=3, decimal_places=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return f"{self.code} - {self.title}"


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sections")
    section_code = models.CharField(max_length=10)  # e.g., A, B
    teacher = models.ForeignKey("accounts.TeacherProfile", on_delete=models.SET_NULL, null=True, blank=True)
    semester = models.CharField(max_length=20)  # e.g., 2025-26 Sem1

    class Meta:
        unique_together = ("course", "section_code", "semester")

    def __str__(self):
        return f"{self.course.code}-{self.section_code} ({self.semester})"
