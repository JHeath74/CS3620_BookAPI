from rest_framework import serializers
from .models import BookData


class BookSerializer(serializers.ModelSerializer):
    Book_Image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = BookData
        fields = ['Book_Name', 'Book_Category', 'Book_ISBN', 'Book_Description', 'Book_Rating', 'Book_Image']
