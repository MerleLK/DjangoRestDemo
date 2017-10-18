"""
    This is the serializes from the model....
"""
# from random import choices
# from datetime import datetime
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response
from apidemo import models


# class Comment:
#     def __init__(self, email, content, created=None):
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    additional_param = serializers.CharField(max_length=20)

    def validate_content(self, value):
        if 'merle' not in value.lower():
            raise serializers.ValidationError("Error not have merle")
        return value

    def create(self, validated_data):
        comment = models.Comment(**validated_data)
        comment.save()
        return Response(comment)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance


class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def validate_title(self, value):
        """
        This is the field_level validation.
        Check the title is about 'django'.
        :param value: title content.
        :return: error or value.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about django")
        return value


class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=200)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    name = serializers.CharField()
    room_number = serializers.ChoiceField(choices=[101, 102, 103, 201])
    date = serializers.DateField()

    # def validate(self, data):
    #     """
    #     This is the object_level validation.
    #     Check the start is before the stop.
    #     :param data: input data
    #     :return: input data
    #     """
    #     if data['start'] > data['finish']:
    #         raise serializers.ValidationError("finish must occur after start.")
    #     return data

    class Meta:
        """ validate the room_number only has one event per day """
        validators = [UniqueTogetherValidator(
            queryset=models.Event.objects.all(),
            fields=['room_number', 'date']
        )]

    def create(self, validated_data):
        event = models.Event(**validated_data)
        event.save()
        return Response("Success!")

    def update(self, instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save(self)
        return instance


# you can do divide the validations.
def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError("Not a multiple of ten")


class GameRecordSerializer(serializers.Serializer):
    """
    Test sentence:

    In [1]: from apidemo.serializers import GameRecordSerializer
    In [2]: seri = GameRecordSerializer(data={'score': 20})
    In [3]: seri.is_valid()
    Out[3]: True
    In [4]: seri.errors
    Out[4]: ReturnDict()

    In [5]: seri = GameRecordSerializer(data={'score': 21})
    In [6]: seri.is_valid()
    Out[6]: False
    In [7]: seri.errors
    Out[7]: ReturnDict([('score', ['Not a multiple of ten'])])
    """
    score = serializers.IntegerField(validators=[multiple_of_ten])

    def create(self, validated_data):
        record = models.GameRecord(**validated_data)
        record.save()
        return record

    def update(self, instance, validated_data):
        instance.score = validated_data.get('score', instance.score)
        return instance

    class Meta:
        model = models.GameRecord
        fields = "__all__"


class ContactFormSerializer(serializers.Serializer):
    """
        you can override the .save() function.
    """
    email = serializers.EmailField()
    message = serializers.CharField(max_length=100)

    def save(self, **kwargs):
        email = self.validated_data["email"]
        message = self.validated_data["message"]
        self.send_email(resource=email, message=message)

    def send_email(self, resource, message):
        pass


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(
        max_length=30,
    )


class EditItemSerializer(serializers.Serializer):
    pass


class PosterSerializer(serializers.Serializer):
    user = UserSerializer()   # if this will be None,  add (required=False)
    edits = EditItemSerializer(many=True)  # if edits is a list, should add param (many=True)

    content = serializers.CharField(
        max_length=120,
    )
    created = serializers.DateTimeField()


class Test(serializers.ModelSerializer):
    pass
