"""
    This is the serializes from the model....
"""
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response
from apidemo import models


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


class MoneyAmountField(serializers.Field):
    def to_internal_value(self, data):
        # to in
        pass

    def to_representation(self, value):
        # to out
        pass


class AccountSerializer(serializers.ModelSerializer):
    amount = MoneyAmountField(source="pur_amount")

    class Meta:
        model = models.Account


class BookListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        book_mapping = {book.id: book for book in instance}
        data_mapping = {item['id']: item for item in validated_data}

        ret = []
        for book_id, data in data_mapping.items():
            book = book_mapping.get(book_id, None)
            if book is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(book, data))

        for book_id, book in book_mapping.items():
            if book_id not in data_mapping:
                book.delete()

        return ret


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    class Meta:
        list_serializer_class = BookListSerializer
