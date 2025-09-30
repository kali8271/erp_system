from rest_framework import serializers
from .models import Exam, Result
from academics.serializers import SectionSerializer
from accounts.serializers import StudentProfileSerializer
from academics.models import Section
from accounts.models import StudentProfile


class ExamSerializer(serializers.ModelSerializer):
    section = SectionSerializer(read_only=True)
    section_id = serializers.PrimaryKeyRelatedField(
        queryset=Section.objects.all(),  # ✅ provide queryset directly
        source="section",
        write_only=True
    )

    class Meta:
        model = Exam
        fields = ["id", "section", "section_id", "title", "date", "max_marks", "created_at"]


class ResultSerializer(serializers.ModelSerializer):
    exam = ExamSerializer(read_only=True)
    exam_id = serializers.PrimaryKeyRelatedField(
        queryset=Exam.objects.all(),  # ✅ provide queryset directly
        source="exam",
        write_only=True
    )

    student = StudentProfileSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=StudentProfile.objects.all(),  # ✅ provide queryset directly
        source="student",
        write_only=True
    )

    class Meta:
        model = Result
        fields = ["id", "exam", "exam_id", "student", "student_id", "marks_obtained", "grade"]
