"""
    This is the serializes from the model....
"""
from datetime import datetime
from rest_framework import serializers


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def validate_content(self, value):
        if 'merle' not in value.lower():
            raise serializers.ValidationError("Error not have merle")
        return value

    def validate(self, data):
        if data['email'] == "11@qq.com":
            raise serializers.ValidationError("Email is error.")
        return data

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance
