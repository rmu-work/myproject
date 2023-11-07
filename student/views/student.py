from myproject.helpers.viewset import CustomModelViewSet

from student.models import Attachments
from student.models import Academics
from student.models import EnglishLanguageRequirement

from student.serializers import AttachmentsSerializer
from student.serializers import AcademicsSerializer
from student.serializers import EnglishLanguageRequirementSerializer


class AttachmentsModelViewSet(CustomModelViewSet):
    queryset = Attachments.objects.all()
    serializer_class = AttachmentsSerializer
    default_fields = ['document_type', 'document', 'uploaded_at']
    search_fields = ['document_type']


class AcademicsModelViewSet(CustomModelViewSet):
    queryset = Academics.objects.all()
    serializer_class = AcademicsSerializer
    default_fields = ['name', 'qualification', 'start_date', 'end_date', 'grade', 'remarks']
    search_fields = ['name', 'qualification']


class EnglishLanguageRequirementModelViewSet(CustomModelViewSet):
    queryset = EnglishLanguageRequirement.objects.all()
    serializer_class = EnglishLanguageRequirementSerializer
    default_fields = ['candidate_id', 'expiry_date']
    search_fields = ['candidate_id', 'expiry_date']
