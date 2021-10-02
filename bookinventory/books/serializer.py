from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'book_name', 'book_author', 'book_count')


class LibrarySerializer(serializers.ModelSerializer):

    book = BookSerializer()

    class Meta:
        model = Library
        fields = ('id', 'book', 'added_on')
