from django.test import TestCase
from django.test.utils import setup_test_environment, override_settings

from myauth.models import CharlistUser
from personages.models import Personage
# Анжель, на досуге добавь тесты, как тут: https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Testing

class PersonageTest(TestCase):
    fixtures = ['personages.json', 'myauth.json']  # можно брать фикстуру из любого неймспейса

    def test_personages_qty(self):  # просто сколько их в дампе БД
        personages_count = Personage.objects.count()
        self.assertEqual(personages_count, 1)

    @override_settings(DEBUG=True)
    def test_main_login_required(self):
        response = self.client.get('/all_personages')
        # По умолчанию http клиент не проходит перенаправления. По этому проверяем так.
        self.assertRedirects(response, '/all_personages/', status_code=301, target_status_code=302)

        # Создадим пользователя
        u = CharlistUser(username="admin1", email="admin@localhost", is_active=True)
        # Пароль надо задавать через метод. Т.к. в таблице хранятся хеши паролей.
        u.set_password("1q2w3e")
        u.save()

        response = self.client.login(username='admin1', password="1q2w3e")  # force login
        self.assertTrue(response)

        # В отличие от response = self.client.get('/all_personages')
        # тут нам нет смысла вручную обрабатывать редиректы. По этому просто ставим follow=True
        # Т.е. проходить все редиректы автоматически.
        response = self.client.get('/all_personages', follow=True)
        self.assertEqual(200, response.status_code)

        # print(response.content.decode())

    @override_settings(DEBUG=True)
    def test_get_personage_detail(self):
        self.client.login(username='user_can_CRUD_personage', password='passwordCRUD')
        response = self.client.get('/personage/details/1/')
        self.assertEqual(200, response.status_code)
        self.assertIn('First', response.content.decode())
