"""
    from https://dup2.org/node/1644..  //1643
"""
from rest_framework import serializers

from simpleDemo import models


class AccountListSerializer(serializers.HyperlinkedModelSerializer):
    """
        Test the serializers write_only.
    """
    password = serializers.CharField(
        style={'input_type': 'password'},
    )
    confirm_password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
    )

    def validate(self, data):
        del data['confirm_password']
        return data

    class Meta:
        model = models.Account
        fields = ('username', 'password', 'confirm_password')
