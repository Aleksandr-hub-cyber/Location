from django.test import TestCase
from ..models import Pass

class PassModelTest(TestCase):

    def test_create_pass(self):
        pass = Pass.objects.create(
            coordinates='[1, 2]',
            elevation=1000,
            name='Test Pass',
            photos='["photo1.jpg", "photo2.jpg"]',
            user_name='John Doe',
            user_email='john.doe@example.com',
            user_phone='+1234567890'
        )
        self.assertEqual(pass.coordinates, '[1, 2]')
        self.assertEqual(pass.elevation, 1000)
        self.assertEqual(pass.name, 'Test Pass')
        self.assertEqual(pass.photos, '["photo1.jpg", "photo2.jpg"]')
        self.assertEqual(pass.user_name, 'John Doe')
        self.assertEqual(pass.user_email, 'john.doe@example.com')
        self.assertEqual(pass.user_phone, '+1234567890')

    def test_update_pass(self):
        pass = Pass.objects.create(
            coordinates='[1, 2]',
            elevation=1000,
            name='Test Pass',
            photos='["photo1.jpg", "photo2.jpg"]',
            user_name='John Doe',
            user_email='john.doe@example.com',
            user_phone='+1234567890'
        )
        pass.coordinates = '[2, 3]'
        pass.elevation = 2000
        pass.name = 'Updated Test Pass'
        pass.photos = '["photo3.jpg", "photo4.jpg"]'
        pass.save()
        self.assertEqual(pass.coordinates, '[2, 3]')
        self.assertEqual(pass.elevation, 2000)
        self.assertEqual(pass.name, 'Updated Test Pass')
        self.assertEqual(pass.photos, '["photo3.jpg", "photo4.jpg"]')

    def test_delete_pass(self):
        pass = Pass.objects.create(
            coordinates='[1, 2]',
            elevation=1000,
            name='Test Pass',
            photos='["photo1.jpg", "photo2.jpg"]',
            user_name='John Doe',
            user_email='john.doe@example.com',
            user_phone='+1234567890'
        )
        pass.delete()
        self.assertEqual(Pass.objects.count(), 0)
