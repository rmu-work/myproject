from myproject.helpers.viewset import CustomModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.models import User

from users.serializers import StudentRegisterModelSerializer
from users.serializers import StudentRegisterRetrieveModelSerializer


class Students(CustomModelViewSet):
    queryset = User.objects.filter(is_university=False)
    serializer_class = StudentRegisterRetrieveModelSerializer
    default_fields = [
        'username', 'first_name', 'last_name', 'email', 'contact_number',
    ]
    search_fields = ['first_name', 'email', 'contact_number']
    include_actions = True
    # multiple_lookup_fields = ['username', 'pk']


class RegisterUser(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = StudentRegisterModelSerializer

