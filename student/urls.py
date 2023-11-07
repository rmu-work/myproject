from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views

urlpatterns = []

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('attachments', views.AttachmentsModelViewSet)
router.register('academics', views.AcademicsModelViewSet)
router.register('englishrequirements', views.EnglishLanguageRequirementModelViewSet)

urlpatterns += router.urls
