from rest_framework import serializers
from .models import Notice
from accounts.serializers import UserSerializer
from accounts.models import User  # direct import

class NoticeSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    created_by_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),  # ✅ provide queryset directly
        source="created_by",
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Notice
        fields = ["id", "title", "content", "created_at", "created_by", "created_by_id", "audience"]
