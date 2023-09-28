from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from main.models import Advert
from main.serializers import AdvertListSerializer


# Create your views here.
class AdvertListAPIView(ListAPIView):
    serializer_class = AdvertListSerializer
    queryset = Advert.objects.select_related('category', 'city')


# Create your views here.
class AdvertDetailAPIView(RetrieveAPIView):
    serializer_class = AdvertListSerializer
    queryset = Advert.objects.select_related('category', 'city')

    def retrieve(self, request, *args, **kwargs):
        advert = self.get_object()
        advert.increment_views_count()
        return super().retrieve(request, *args, **kwargs)
