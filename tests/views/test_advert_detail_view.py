from unittest import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase

from main.serializers import AdvertListSerializer
from tests.factories import AdvertFactory


class TestAdvertDetailView(APITestCase):

    def test_retrieve_make_single_query(self):
        """
        Test number of queries is equal to 3
        1) Get object to update
        2) Update
        3) Retrieve
        :return:
        """
        advert = AdvertFactory()
        with self.assertNumQueries(3):
            self.client.get(
                reverse('advert_detail', kwargs={'pk': advert.id})
            )

    def test_retrieve_increments_view_count(self):
        advert = AdvertFactory()
        self.assertEqual(advert.views, 0)
        self.client.get(
            reverse('advert_detail', kwargs={'pk': advert.id})
        )

        advert.refresh_from_db()
        self.assertEqual(advert.views, 1)
