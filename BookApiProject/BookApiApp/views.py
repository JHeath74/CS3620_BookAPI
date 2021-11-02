from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BookSerializer
from .models import BookData


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class CategoryViewSetScienceFiction(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="ScienceFiction")
    serializer_class = BookSerializer


class CategoryViewSetAction(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="Action")
    serializer_class = BookSerializer


class CategoryViewSetAdventure(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="Adventure")
    serializer_class = BookSerializer


class CategoryViewSetClassics(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="Classics")
    serializer_class = BookSerializer


class CategoryViewSetComics(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="Comics")
    serializer_class = BookSerializer


class CategoryViewSetMystery(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="Mystery")
    serializer_class = BookSerializer


class CategoryViewSetFantasy(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="Fantasy")
    serializer_class = BookSerializer


class CategoryViewSetHistoricalFiction(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="HistoricalFiction")
    serializer_class = BookSerializer


class CategoryViewSetHorror(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="Horror")
    serializer_class = BookSerializer


class CategoryViewSetRomance(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="Romance")
    serializer_class = BookSerializer


class CategoryViewSetShortStories(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="ShortStories")
    serializer_class = BookSerializer


class CategoryViewSetThrillers(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="Thrillers")
    serializer_class = BookSerializer


class CategoryViewSetBiographies(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="Biographies")
    serializer_class = BookSerializer


class CategoryViewSetHistory(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="History")
    serializer_class = BookSerializer


class CategoryViewSetPoetry(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="Poetry")
    serializer_class = BookSerializer


class CategoryViewSetCooking(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Book_Category="Cooking")
    serializer_class = BookSerializer
