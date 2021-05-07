from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from snippets.models import Snippet

SNIPPET_HIGHLIGHT = 'snippet-highlight'
SNIPPET_DETAIL = 'snippet-detail'
SNIPPET_LIST = 'snippet-list'

class SnippetUrlTestCase(APITestCase):
    user = None
    admin = None
    admin_plain_password = "admin"
    user_plain_password = "user"
    snippet1 = None
    snippet2 = None

    def setUp(self):
        self.user = User.objects.create_user('testUser', 'test@test.com', self.user_plain_password)
        self.admin = User.objects.create_superuser('admin', 'admin@admin.fr', self.admin_plain_password)
        self.snippet1 = Snippet.objects.create(code='test = "bar"\n', title='test1', owner=self.user)
        self.snippet2 = Snippet.objects.create(code='print("hello, world2")\n', title='test2', owner=self.admin)

    def test_get_all_snippets_OK_admin(self):
        """
        Ensure superuser can view the list of snippets object.
        """
        url = reverse(SNIPPET_LIST)
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_snippets_OK_user(self):
        """
        Ensure user can view the list of snippets object.
        """
        url = reverse(SNIPPET_LIST)
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_snippets_OK_unauthenficated(self):
        """
        Ensure unauthenticated user can view the list of snippet object.
        """
        url = reverse(SNIPPET_LIST)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_all_snippets_put_NOT_ALLOWED_admin(self):
        """
        Ensure superuser cannot edit the list of snippets object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test5'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_all_snippets_put_NOT_ALLOWED_user(self):
        """
        Ensure user cannot edit the list of snippets object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test5'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_all_snippets_put_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user cannot edit the list of snippets object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test5'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_all_snippets_put_NOT_ALLOWED_admin(self):
        """
        Ensure superuser cannot edit the list of snippets object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test5'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update_all_snippets_put_NOT_ALLOWED_user(self):
        """
        Ensure user cannot edit the list of snippets object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test5'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update_all_snippets_put_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user cannot edit the list of snippets object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test5'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_snippet_OK_admin(self):
        """
        Ensure superuser can create a new snippet object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test6'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_snippet_OK_user(self):
        """
        Ensure user can create a new snippet object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test7'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_snippet_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user cannot create a new snippet object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test8'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_snippet_test1_OK_admin(self):
        """
        Ensure superuser can view the snippet 'test1' object.
        """
        idTest1 = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[idTest1])
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_snippet_test1_user(self):
        """
        Ensure user can view the list of snippets object.
        """
        idTest1 = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[idTest1])
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_snippet_test1_unauthenficated(self):
        """
        Ensure unauthenticated user can view the list of snippet object.
        """
        idTest1 = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[idTest1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_snippet_test1_OK_admin(self):
        """
        Ensure superuser update view the snippet created by him.
        """
        idTest1 = self.snippet2.id
        url = reverse(SNIPPET_DETAIL, args=[idTest1])
        data = {'code': 'test2 revu'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Snippet.objects.get(id=idTest1).code, 'test2 revu')

    def test_update_snippet_test1_OK_user(self):
        """
        Ensure user update view the snippet created by him.
        """
        id_test = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[id_test])
        data = {'code': 'test1 revu'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Snippet.objects.get(id=id_test).code, 'test1 revu')

    def test_update_snippet_test1_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenficated user cannot update view the snippet.
        """
        id_test = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[id_test])
        data = {'code': 'test1 revu'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_snippet_test1_FORBIDDEN_admin(self):
        """
        Ensure superuser cannot update view the snippet created by other.
        """
        idTest1 = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[idTest1])
        data = {'code': 'test2 revu'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_snippet_test1_FORBIDDEN_user(self):
        """
        Ensure user cannot update view the snippet created by other.
        """
        idTest1 = self.snippet2.id
        url = reverse(SNIPPET_DETAIL, args=[idTest1])
        data = {'code': 'test2 revu'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_snippet_test1_OK_admin(self):
        """
        Ensure superuser update view the snippet created by him.
        """
        idTest1 = self.snippet2.id
        url = reverse(SNIPPET_DETAIL, args=[idTest1])
        data = {'code': 'test2 revu'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Snippet.objects.get(id=idTest1).code, 'test2 revu')

    def test_partial_update_snippet_test1_OK_user(self):
        """
        Ensure user update view the snippet created by him.
        """
        id_test = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[id_test])
        data = {'code': 'test1 revu'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Snippet.objects.get(id=id_test).code, 'test1 revu')

    def test_partial_update_snippet_test1_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenficated user cannot update view the snippet.
        """
        id_test = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[id_test])
        data = {'code': 'test1 revu'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_snippet_test1_FORBIDDEN_admin(self):
        """
        Ensure superuser cannot update view the snippet created by other.
        """
        idTest1 = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[idTest1])
        data = {'code': 'test2 revu'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_snippet_test1_FORBIDDEN_user(self):
        """
        Ensure user cannot update view the snippet created by other.
        """
        idTest1 = self.snippet2.id
        url = reverse(SNIPPET_DETAIL, args=[idTest1])
        data = {'code': 'test2 revu'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_snippet_highlight_test1_OK_admin(self):
        """
        Ensure superuser can view the snippet 'test1' highlight.
        """
        idTest1 = self.snippet1.id
        url = reverse(SNIPPET_HIGHLIGHT, args=[idTest1])
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_snippet_highlight_test1_OK_user(self):
        """
        Ensure superuser can view the snippet 'test1' highlight.
        """
        idTest1 = self.snippet1.id
        url = reverse(SNIPPET_HIGHLIGHT, args=[idTest1])
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_snippet_highlight_test1_OK_unauthenficated(self):
        """
        Ensure superuser can view the snippet 'test1' highlight.
        """
        idTest1 = self.snippet1.id
        url = reverse(SNIPPET_HIGHLIGHT, args=[idTest1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
