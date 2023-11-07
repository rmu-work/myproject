from myproject.helpers.viewset import CustomModelViewSet

from masterdata.models import ELRCertificates
from masterdata.seializers import ELRCertificatesSerializers


class ELRCertificatesModelViewSet(CustomModelViewSet):
    queryset = ELRCertificates.objects.all()
    serializer_class = ELRCertificatesSerializers
    default_fields = ['name', 'total_subjects', 'mark_out_of']
    search_fields = ['name']