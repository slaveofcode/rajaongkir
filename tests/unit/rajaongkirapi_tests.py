import unittest, os, sys
from unittest import TestCase

current_dir = os.path.dirname(__file__)
base_dir = os.path.join(current_dir, os.pardir, os.pardir)
sys.path.append(base_dir)

from api import RajaOngkirApi

api_key = u'SetYourApiKeyHereBeforeRunningTest'


class RajaOngkirTests(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = RajaOngkirApi(api_key)
        super(RajaOngkirTests, cls).setUpClass()

    def test_provinces(self):
        provinces = self.api.provinces()
        self.assertEqual(type(provinces), list)

    def test_province_by_id(self):
        provinces = self.api.province_by_id(9)  # Jawa Barat
        self.assertEqual(type(provinces), dict)

    def test_cities(self):
        cities = self.api.cities()
        self.assertEqual(type(cities), list)

    def test_city_by_id(self):
        city = self.api.city_by_id(1)
        self.assertEqual(type(city), dict)

    def test_city_by_province_and_city_id(self):
        city = self.api.city_by_province_and_city(9, 55)  # Jawa Barat, Bekasi
        self.assertEqual(type(city), dict)

    def test_city_by_province(self):
        city = self.api.city_by_province(9)  # Jawa Barat
        self.assertEqual(type(city), list)

    def test_cost_between_city(self):
        cost = self.api.cost_between_city(55, 23, 1000)  # from bekasi to bandung with 1 kg weight
        self.assertEqual(type(cost), list)


if __name__ == '__main__':
    unittest.main()