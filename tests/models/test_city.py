from django.db import IntegrityError
from django.test import TestCase

from tests.factories import CityFactory


class TestCityModel(TestCase):
    def test_name_must_be_unique(self):
        with self.assertRaises(IntegrityError):
            CityFactory.create_batch(2, name='Not unique')
