from rest_framework import serializers
from .models import Attendance
from accounts.serializers import StudentProfileSerializer
from academics.serializers import SectionSerializer
from accounts.models import StudentProfile
from academics.models import Section


class AttendanceSerializer(serializers.ModelSerializer):
    section = SectionSerializer(read_only=True)
    section_id = serializers.PrimaryKeyRelatedField(
        queryset=Section.objects.all(),  # ✅ provide queryset directly
        source="section",
        write_only=True
    )

    student = StudentProfileSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=StudentProfile.objects.all(),  # ✅ provide queryset directly
        source="student",
        write_only=True
    )

    class Meta:
        model = Attendance
        fields = ["id", "section", "section_id", "student", "student_id", "date", "status", "marked_at"]
