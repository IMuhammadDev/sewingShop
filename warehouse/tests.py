from rest_framework.test import APITestCase
from rest_framework import status
from .models import Mahsulot, Xomashyo, MahsulotXomashyo, Omborxona


class MahsulotTests(APITestCase):
    def test_create_mahsulot(self):
        data = {'nom': 'Test Mahsulot', 'kod': '123456'}
        response = self.client.post('/api/mahsulotlar/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mahsulot.objects.count(), 1)
        self.assertEqual(Mahsulot.objects.get().nom, 'Test Mahsulot')


class XomashyoTests(APITestCase):
    def test_create_xomashyo(self):
        data = {'nom': 'Test Xomashyo'}
        response = self.client.post('/api/xomashyolar/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Xomashyo.objects.count(), 1)
        self.assertEqual(Xomashyo.objects.get().nom, 'Test Xomashyo')


class MahsulotXomashyoTests(APITestCase):
    def test_create_mahsulot_xomashyo(self):
        mahsulot = Mahsulot.objects.create(nom='Test Mahsulot', kod='123456')
        xomashyo = Xomashyo.objects.create(nom='Test Xomashyo')
        data = {'mahsulot': mahsulot.id, 'xomashyo': xomashyo.id, 'miqdori': 10}
        response = self.client.post('/api/mahsulot-xomashyolar/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MahsulotXomashyo.objects.count(), 1)
        self.assertEqual(MahsulotXomashyo.objects.get().miqdori, 10)


class OmborxonaTests(APITestCase):
    def test_create_omborxona(self):
        xomashyo = Xomashyo.objects.create(nom='Test Xomashyo')
        data = {'xomashyo': xomashyo.id, 'qolgan_miqdori': 50, 'narx': 100.0}
        response = self.client.post('/api/omborxonalar/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Omborxona.objects.count(), 1)
        self.assertEqual(Omborxona.objects.get().qolgan_miqdori, 50)
