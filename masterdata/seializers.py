from rest_framework import serializers
from masterdata.models import Qualifications
from masterdata.models import FinancialDocumentTypes
from masterdata.models import ELRCertificates


class QualificationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Qualifications
        fields = '__all__'


class FinancialDocumentTypesSerializers(serializers.ModelSerializer):
    class Meta:
        model = FinancialDocumentTypes
        fields = '__all__'


class ELRCertificatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ELRCertificates
        fields = '__all__'

