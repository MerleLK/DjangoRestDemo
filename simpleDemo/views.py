from rest_framework import mixins, generics, viewsets
from rest_framework.serializers import ValidationError
from rest_framework.response import Response


from simpleDemo import models, serializers


class AccountViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountListSerializer

    def list(self, request, *args, **kwargs):
        serializer = serializers.AccountListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if not request.query_params.get('password') or request.query_params.get('confirm_password'):
            raise ValidationError("input password and confirm it!")
        if request.query_params.get('password') != request.query_params.get('confirm_password'):
            raise ValidationError("passwords not match!")
        serializer = serializers.AccountListSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pass
