from django.db import IntegrityError
from django.test import TestCase

from tests.factories import CategoryFactory


class TestCategoryModel(TestCase):
    def test_name_must_be_unique(self):
        with self.assertRaises(IntegrityError):
            CategoryFactory.create_batch(2, name='Not unique')
