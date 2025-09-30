from django.db import models
from django.utils import timezone


class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True, blank=True)
    audience = models.CharField(
        max_length=20,
        choices=[
            ("all", "All"),
            ("students", "Students"),
            ("teachers", "Teachers"),
            ("admins", "Administrators"),
            ("chancellor", "Chancellor"),
        ],
        default="all",
    )

    def __str__(self):
        return f"{self.title} ({self.audience})"
