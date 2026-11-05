from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from .models import Book,BorrowRecord
from django.db import transaction

class BookSerializer(ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
        read_only_fields=["id"]

class BorrowRecordSerializer(ModelSerializer):
    book_title = serializers.SerializerMethodField()
    class Meta:
        model=BorrowRecord
        fields="__all__"
    def get_book_title(self, obj):
        return obj.book.title
    
    def validate_book(self, value):

        if value.available_copies <= 0:
            raise Serializer.ValidationError(
                "This book is currently unavailable. No copies are left."
            )

        return value

    @transaction.atomic
    def create(self, validated_data):

        book = validated_data['book']
        book.available_copies -= 1
        book.save()
        borrow_record = BorrowRecord.objects.create(**validated_data)
        

        