from myproject.helpers.viewset import CustomModelViewSet

from masterdata.models import Qualifications
from masterdata.seializers import QualificationsSerializers


class QualificationsModelViewSet(CustomModelViewSet):
    queryset = Qualifications.objects.all()
    serializer_class = QualificationsSerializers
    default_fields = ['name', 'description']
    search_fields = ['name']


