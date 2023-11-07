from rest_framework import serializers

from .models import Attachments
from .models import Academics
from .models import EnglishLanguageRequirement


class AttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachments
        fields = '__all__'


class AcademicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academics
        fields = '__all__'


class EnglishLanguageRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishLanguageRequirement
        fields = '__all__'
