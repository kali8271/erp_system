from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, StudentProfile, TeacherProfile


@receiver(post_save, sender=User)
def create_role_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == User.Role.STUDENT:
            StudentProfile.objects.create(
                user=instance, roll_no=f"STU{instance.id:05d}"
            )
        elif instance.role == User.Role.TEACHER:
            TeacherProfile.objects.create(
                user=instance, employee_id=f"TCH{instance.id:05d}"
            )
