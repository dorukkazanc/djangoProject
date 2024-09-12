from django.test import TestCase
from django.urls import reverse

from users.models import User


class UsersTestCase(TestCase):
    # Mock user objesi oluşturulur
    def setUp(self):
        self.user = User.objects.create(name='Test User',
                                        username='Test adı',
                                        address={},
                                        company={},
                                        website='test.com',
                                        phone='1234567890',
                                        email='test@test.com')

    # Oluşturulan mock user objesi ile album oluşturulur ve test edilir
    def test_create_album(self):
        url = '/api/albums/'
        data = {
            'userId': self.user.id,
            'title': 'Test Albüm'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['userId'], self.user.id)
        self.assertEqual(response.data['title'], 'Test Albüm')

