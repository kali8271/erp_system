from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        TEACHER = "teacher", "Teacher"
        ADMIN = "admin", "Administrator"
        CHANCELLOR = "chancellor", "Chancellor"

    role = models.CharField(
        max_length=20, choices=Role.choices, default=Role.STUDENT
    )
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")
    roll_no = models.CharField(max_length=30, unique=True)
    program = models.CharField(max_length=120)
    year = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.roll_no}"


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher")
    employee_id = models.CharField(max_length=30, unique=True)
    department = models.CharField(max_length=120)
    designation = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.employee_id}"
