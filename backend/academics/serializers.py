from rest_framework import serializers
from .models import Department, Course, Section
from accounts.serializers import TeacherProfileSerializer
from accounts.models import TeacherProfile  # directly import the model


# -------------------- Department Serializer --------------------
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "code", "name"]


# -------------------- Course Serializer --------------------
class CourseSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source="department", write_only=True
    )

    class Meta:
        model = Course
        fields = ["id", "code", "title", "credits", "department", "department_id"]


# -------------------- Section Serializer --------------------
class SectionSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source="course", write_only=True
    )

    teacher = TeacherProfileSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=TeacherProfile.objects.all(),  # ✅ directly provide queryset
        source="teacher",
        write_only=True,
        allow_null=True
    )

    class Meta:
        model = Section
        fields = [
            "id",
            "course",
            "course_id",
            "section_code",
            "teacher",
            "teacher_id",
            "semester",
        ]
