from django.urls import path
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views
from . import rest_views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('register-user', rest_views.RegisterUser)
router.register('students', rest_views.Students)
router.register('university', rest_views.UniversityModelViewSet)

urlpatterns = [
    path('login/', views.Login.as_view(), name='user-login')
]

urlpatterns += router.urls