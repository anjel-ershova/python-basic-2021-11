from django.contrib.auth import get_user_model  # возвращает актуальную модель пользователя
from django.test import TestCase
from django.urls import reverse

from django.utils.translation import gettext_lazy as _


class CharlistUserRegisterTest(TestCase):  # внутри TestCase уже создан Client
    # fixtures = ['myauth.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.vaild_user_data = {
            'username': 'test_user_valid',
            'email': 'admin@otus.local',
            'password1': 'OtusOtus',
            'password2': 'OtusOtus',
        }
        cls.user_broken_data = {
            'username': 'test_user_incorrect_pass2',
            'email': 'admin@otus.local',
            'password1': 'OtusOtus',
            'password2': 'Otus',
        }

    def test_success_register(self):
        response = self.client.post(
            '/myauth/register/',
            data=self.vaild_user_data
        )
        print(response.content.decode())
        self.assertEqual(302, response.status_code)

        new_user = get_user_model().objects.get(
            username=self.vaild_user_data['username']
        )

        self.assertEqual(self.vaild_user_data['email'],
                         new_user.email)

    def test_fail_register(self):
        response = self.client.post(
            reverse('myauth:register'),  # reverse сам реконструирует адрес.Идет в пр-во имен,ищет urls-->указанный name
                                        # можно передавать *args, **kwargs если урл динамический
            data=self.user_broken_data
        )
        self.assertEqual(200, response.status_code)
        self.assertFormError(
            response,
            'form',
            'password2',
            _('The two password fields didn’t match.')
            # 'Введенные пароли не совпадают.'
        )
