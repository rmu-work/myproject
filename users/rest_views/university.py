from myproject.helpers.viewset import CustomModelViewSet

from users.models import User

from users.serializers import UniversitySerializer
from users.serializers import UniversityRetrieveSerializer


class UniversityModelViewSet(CustomModelViewSet):
    queryset = User.objects.filter(is_university=True)
    serializer_class = UniversitySerializer
    default_fields = [
        'university_name', 'university_id', 'website',
        'contact_number',
    ]
    search_fields = ['university_name', 'university_id']

    def get_serializer_class(self):
        if self.action == 'list':
            return UniversityRetrieveSerializer
        return super().get_serializer_class()
