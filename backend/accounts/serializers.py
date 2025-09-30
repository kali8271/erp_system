from rest_framework import serializers
from .models import User, StudentProfile, TeacherProfile


# -------------------- User Serializer --------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "role"]


# -------------------- Student Profile Serializer --------------------
class StudentProfileSerializer(serializers.ModelSerializer):
    # User is read-only nested
    user = UserSerializer(read_only=True)

    class Meta:
        model = StudentProfile
        fields = ["id", "user", "roll_no", "program", "year"]


# -------------------- Teacher Profile Serializer --------------------
class TeacherProfileSerializer(serializers.ModelSerializer):
    # User is read-only nested
    user = UserSerializer(read_only=True)

    class Meta:
        model = TeacherProfile
        fields = ["id", "user", "employee_id", "department", "designation"]
