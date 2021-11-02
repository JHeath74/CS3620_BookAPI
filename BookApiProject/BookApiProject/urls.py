"""BookApiProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from BookApiApp.views import BookViewSet, CategoryViewSetScienceFiction, CategoryViewSetAction,\
    CategoryViewSetAdventure, CategoryViewSetClassics, CategoryViewSetComics, CategoryViewSetMystery, \
    CategoryViewSetFantasy, CategoryViewSetHistoricalFiction, CategoryViewSetHorror, CategoryViewSetRomance,\
    CategoryViewSetShortStories, CategoryViewSetThrillers, CategoryViewSetBiographies, CategoryViewSetHistory,\
    CategoryViewSetPoetry, CategoryViewSetCooking
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('BookApiApp', BookViewSet)
router.register('ScienceFiction', CategoryViewSetScienceFiction)
router.register('Action', CategoryViewSetAction)
router.register('Adventure', CategoryViewSetAdventure)
router.register('Classics', CategoryViewSetClassics)
router.register('Comics', CategoryViewSetComics)
router.register('Mystery', CategoryViewSetMystery)
router.register('Fantasy', CategoryViewSetFantasy)
router.register('Fiction', CategoryViewSetHistoricalFiction)
router.register('Horror', CategoryViewSetHorror)
router.register('Romance', CategoryViewSetRomance)
router.register('ShortStories', CategoryViewSetShortStories)
router.register('Thrillers', CategoryViewSetThrillers)
router.register('Biographies', CategoryViewSetBiographies)
router.register('History', CategoryViewSetHistory)
router.register('Poetry', CategoryViewSetPoetry)
router.register('Cooking', CategoryViewSetCooking)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
