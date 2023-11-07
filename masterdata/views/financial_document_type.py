from myproject.helpers.viewset import CustomModelViewSet

from masterdata.models import FinancialDocumentTypes
from masterdata.seializers import FinancialDocumentTypesSerializers


class FinancialDocumentTypesModelViewSet(CustomModelViewSet):
    queryset = FinancialDocumentTypes.objects.all()
    serializer_class = FinancialDocumentTypesSerializers
    default_fields = ['name', 'description']
    search_fields = ['name']