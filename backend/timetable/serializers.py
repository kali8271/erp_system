from rest_framework import serializers
from .models import Room, Timetable
from academics.serializers import CourseSerializer, SectionSerializer
from accounts.serializers import TeacherProfileSerializer
from academics.models import Course, Section
from accounts.models import TeacherProfile

# -------------------- Room --------------------
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


# -------------------- Timetable --------------------
class TimetableSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source="course",
        write_only=True
    )

    section = SectionSerializer(read_only=True)
    section_id = serializers.PrimaryKeyRelatedField(
        queryset=Section.objects.all(),
        source="section",
        write_only=True
    )

    teacher = TeacherProfileSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=TeacherProfile.objects.all(),
        source="teacher",
        write_only=True
    )

    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(),
        source="room",
        write_only=True,
        allow_null=True
    )

    class Meta:
        model = Timetable
        fields = [
            "id",
            "course", "course_id",
            "section", "section_id",
            "teacher", "teacher_id",
            "room", "room_id",
            "day_of_week", "start_time", "end_time"
        ]
