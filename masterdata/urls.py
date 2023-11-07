from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views

urlpatterns = []

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('qualifications', views.QualificationsModelViewSet)
router.register('financialdocumenttype', views.FinancialDocumentTypesModelViewSet)
router.register('elrcertificate', views.ELRCertificatesModelViewSet)

urlpatterns += router.urls
