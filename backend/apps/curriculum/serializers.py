from rest_framework import serializers
from enumfields.drf.serializers import EnumSupportSerializerMixin
from .models import Lesson


class LessonSerializer(EnumSupportSerializerMixin, serializers.ModelSerializer):
    """The Lesson Serializer with educator full name
    """
    educator_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = [
            'id',
            'educator_id',
            'educator_full_name',
            'subject',
            'created_at',
            'grade_level',
            'title',
            'text',
            'video_link'
        ]
        read_only_fields = ['educator_id', 'educator_full_name']

    def get_educator_full_name(self, obj):
        """Get full name of the educator"""
        return f"{obj.educator_id.first_name} {obj.educator_id.last_name}"
