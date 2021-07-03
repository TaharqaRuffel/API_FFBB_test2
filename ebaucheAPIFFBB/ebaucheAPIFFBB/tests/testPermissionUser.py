from django.urls import reverse
from rest_framework.authtoken.admin import User
from rest_framework.test import APITestCase
from rest_framework import status


USER_DETAIL = 'user-detail'
USER_LIST = 'user-list'

class UserUrlTestCase(APITestCase):
    user = None
    admin = None
    admin_plain_password = "admin"
    user_plain_password = "user"

    def setUp(self):
        self.user = User.objects.create_user('testUser', 'test@test.com', self.user_plain_password)
        self.admin = User.objects.create_superuser('admin', 'admin@admin.fr', self.admin_plain_password)

    def test_get_all_users_OK_admin(self):
        """
        Ensure superuser can view the list of users object.
        """
        url = reverse(USER_LIST)
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_users_FORBIDDEN_user(self):
        """
        Ensure user cannot view the list of users .
        """
        url = reverse(USER_LIST)
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_all_users_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user can view the list of users object.
        """
        url = reverse(USER_LIST)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_all_users_put_NOT_ALLOWED_admin(self):
        """
        Ensure superuser cannot edit the list of users object.
        """
        url = reverse(USER_LIST)
        data = {'username': 'testUser', 'email': 'test@test.com', 'password': 'test'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_all_users_put_NOT_ALLOWED_user(self):
        """
        Ensure user cannot edit the list of users object.
        """
        url = reverse(USER_LIST)
        data = {'code': 'test5'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_all_users_put_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user cannot edit the list of users object.
        """
        url = reverse(USER_LIST)
        data = {'code': 'test5'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_user_OK_admin(self):
        """
        Ensure superuser can view a specific user.
        """
        idTest1 = self.user.id
        url = reverse(USER_DETAIL, args=[idTest1])
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_FORBIDDEN_user(self):
        """
        Ensure user cannot view the list of users .
        """
        idTest1 = self.user.id
        url = reverse(USER_DETAIL, args=[idTest1])
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_user_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user can view the list of users object.
        """
        idTest1 = self.user.id
        url = reverse(USER_DETAIL, args=[idTest1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_user_put_NOT_ALLOWED_admin(self):
        """
        Ensure superuser cannot edit the list of users object.
        """
        idTest1 = self.user.id
        url = reverse(USER_DETAIL, args=[idTest1])
        data = {'username': 'testUser', 'email': 'test@test.com', 'password': 'test'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_put_NOT_ALLOWED_user(self):
        """
        Ensure user cannot edit the list of users object.
        """
        idTest1 = self.user.id
        url = reverse(USER_DETAIL, args=[idTest1])
        data = {'code': 'test5'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_user_put_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user cannot edit the list of users object.
        """
        idTest1 = self.user.id
        url = reverse(USER_DETAIL, args=[idTest1])
        data = {'code': 'test5'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
