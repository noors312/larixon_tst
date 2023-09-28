from unittest import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase

from main.serializers import AdvertListSerializer
from tests.factories import AdvertFactory


class TestAdvertListView(APITestCase):
    def setUp(self) -> None:
        self.data = AdvertFactory.create_batch(10)

    def test_advert_list_response_data(self):
        expected_result = AdvertListSerializer(self.data, many=True).data
        response = self.client.get(reverse('advert_list'))

        self.assertEqual(response.data, expected_result)

    def test_advert_list_make_single_query(self):
        with self.assertNumQueries(1):
            self.client.get(reverse('advert_list'), data={'format': 'json'})
