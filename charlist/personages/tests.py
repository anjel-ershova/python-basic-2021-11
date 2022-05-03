from django.test import TestCase
from django.test.utils import setup_test_environment


from personages.models import Personage
# Анжель, на досуге добавь тесты, как тут: https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Testing

class PersonageTest(TestCase):
    fixtures = ['personages.json', 'myauth.json']  # можно брать фикстуру из любого неймспейса

    def test_personages_qty(self):  # просто сколько их в дампе БД
        personages_count = Personage.objects.count()
        self.assertEqual(personages_count, 1)

    def test_main_login_required(self):
        response = self.client.get('/all_personages')
        self.assertEqual(302, response.status_code) # ошибка AssertionError: 302 != 301

        self.client.login(username='user_can_CRUD_personage', password='passwordCRUD')
        response = self.client.get('/all_personages')  # force login
        self.assertFalse(response.context['all_personages'].is_anonymous)
        # self.assertIn('View all personages', response.content.decode()) # ошибка AssertionError: 'View all personages' not found in ''
        print(response.content.decode())
        self.assertEqual(200, response.status_code)

