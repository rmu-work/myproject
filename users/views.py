from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import LoginSerializer


class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        serializer = LoginSerializer(data=self.request.data, **{'request': self.request})

        if serializer.is_valid(raise_exception=True):
            serializer.login(self.request)

            return Response({
                'success': True,
                'message': 'Successfully logined'
            }, status.HTTP_200_OK)

