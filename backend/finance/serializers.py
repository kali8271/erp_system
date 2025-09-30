from rest_framework import serializers
from .models import Fee, Payment, Scholarship, Fine
from accounts.serializers import StudentProfileSerializer
from accounts.models import StudentProfile  # direct import


# -------------------- Fee Serializer --------------------
class FeeSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=StudentProfile.objects.all(),  # ✅ provide queryset directly
        source="student",
        write_only=True
    )

    class Meta:
        model = Fee
        fields = ["id", "student", "student_id", "amount", "due_date", "description", "is_paid", "created_at"]


# -------------------- Payment Serializer --------------------
class PaymentSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=StudentProfile.objects.all(),
        source="student",
        write_only=True
    )

    class Meta:
        model = Payment
        fields = ["id", "student", "student_id", "fee", "amount", "payment_date", "method", "reference"]


# -------------------- Scholarship Serializer --------------------
class ScholarshipSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=StudentProfile.objects.all(),
        source="student",
        write_only=True
    )

    class Meta:
        model = Scholarship
        fields = ["id", "student", "student_id", "name", "amount", "awarded_date"]


# -------------------- Fine Serializer --------------------
class FineSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=StudentProfile.objects.all(),
        source="student",
        write_only=True
    )

    class Meta:
        model = Fine
        fields = ["id", "student", "student_id", "reason", "amount", "issued_date", "is_paid"]
