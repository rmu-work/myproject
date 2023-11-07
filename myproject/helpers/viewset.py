from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from myproject.helpers.utils import generate_column
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CustomModelViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet
):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    queryset = None
    default_fields = []
    include_actions = True
    multiple_lookup_fields = []

    @action(detail=False, methods=['POST'])
    def create_record(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_db_action(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'])
    def update_record(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_db_action(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=['POST', 'DELETE'])
    def delete_record(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_delete(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_db_action(self, serializer):
        serializer.save()

    def perform_delete(self, instance):
        instance.delete()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        try:
            response.data['columns'] = generate_column(
                self.queryset.model, actions=self.include_actions,
                default_fields=self.default_fields
            )
        except Exception as e:
            print('Exception occurred while generating the columns : ', e)
        return response

    # def get_object(self):
    #     queryset = self.get_queryset()
    #     or_condition = Q()
    #     for field in self.multiple_lookup_fields:
    #         or_condition.add(Q(**{field: self.kwargs['pk']}), Q.OR)
    #     obj = get_object_or_404(queryset, or_condition)
    #     return obj
