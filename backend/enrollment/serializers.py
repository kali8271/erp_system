from rest_framework import serializers
from .models import Enrollment
from accounts.serializers import StudentProfileSerializer
from academics.serializers import SectionSerializer
from accounts.models import StudentProfile
from academics.models import Section


class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=StudentProfile.objects.all(),
        source="student",
        write_only=True
    )

    section = SectionSerializer(read_only=True)
    section_id = serializers.PrimaryKeyRelatedField(
        queryset=Section.objects.all(),
        source="section",
        write_only=True
    )

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student",
            "student_id",
            "section",
            "section_id",
            "enrollment_date",
            "status",
        ]
