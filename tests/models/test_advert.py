from django.db import IntegrityError
from django.test import TestCase

from main.models import Category, City
from tests.factories import AdvertFactory


class TestAdvertModel(TestCase):
    def test_increment_views_count(self):
        advert = AdvertFactory(views=3)
        self.assertEqual(advert.views, 3)

        advert.increment_views_count()
        advert.refresh_from_db()

        self.assertEqual(advert.views, 4)

    def test_views_cant_be_negative(self):
        with self.assertRaises(IntegrityError):
            AdvertFactory(views=-3)

    def test_city_is_null_on_city_delete(self):
        advert = AdvertFactory()
        self.assertNotEqual(advert.city, None)

        city = advert.city
        city.delete()

        with self.assertRaises(City.DoesNotExist):
            City.objects.get(id=city.id)

        advert.refresh_from_db()

        self.assertEqual(advert.city, None)

    def test_category_is_null_on_city_delete(self):
        advert = AdvertFactory()
        self.assertNotEqual(advert.category, None)

        category = advert.category
        category.delete()

        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=category.id)

        advert.refresh_from_db()

        self.assertEqual(advert.category, None)
