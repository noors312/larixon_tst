from django.urls import path

from main.views import AdvertListAPIView, AdvertDetailAPIView

urlpatterns = [
    path('advert-list', AdvertListAPIView.as_view(), name='advert_list'),
    path(
        'advert/<int:pk>', AdvertDetailAPIView.as_view(),
        name='advert_detail'
    ),
]
