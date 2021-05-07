from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from snippets.models import Match

class MatchUrlTestCase(APITestCase):
    user = None
    admin = None
    admin_plain_password = "admin"
    user_plain_password = "user"
    match1 = None
    match2 = None

    def setUp(self):
        self.user = User.objects.create_user('testUser', 'test@test.com', self.user_plain_password)
        self.admin = User.objects.create_superuser('admin', 'admin@admin.fr', self.admin_plain_password)
        self.match1 = Match.objects.create(code='test = "bar"\n', title='test1', owner=self.user)
        self.match2 = Match.objects.create(code='print("hello, world2")\n', title='test2', owner=self.admin)

    # def test_get_all_matches_OK_admin(self):
    #     """
    #     Ensure superuser can view the list of matches object.
    #     """
    #     url = reverse(SNIPPET_LIST)
    #     self.client.login(username=self.admin.username, password=self.admin_plain_password)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_get_all_matches_OK_user(self):
    #     """
    #     Ensure user can view the list of matches object.
    #     """
    #     url = reverse(SNIPPET_LIST)
    #     self.client.login(username=self.admin.username, password=self.admin_plain_password)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_get_all_matches_OK_unauthenficated(self):
    #     """
    #     Ensure unauthenticated user can view the list of match object.
    #     """
    #     url = reverse(SNIPPET_LIST)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_update_all_matches_put_NOT_ALLOWED_admin(self):
    #     """
    #     Ensure superuser cannot edit the list of matches object.
    #     """
    #     url = reverse(SNIPPET_LIST)
    #     data = {'code': 'test5'}
    #     self.client.login(username=self.admin.username, password=self.admin_plain_password)
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    #
    # def test_update_all_matches_put_NOT_ALLOWED_user(self):
    #     """
    #     Ensure user cannot edit the list of matches object.
    #     """
    #     url = reverse(SNIPPET_LIST)
    #     data = {'code': 'test5'}
    #     self.client.login(username=self.user.username, password=self.user_plain_password)
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    #
    # def test_update_all_matches_put_FORBIDDEN_unauthenficated(self):
    #     """
    #     Ensure unauthenticated user cannot edit the list of matches object.
    #     """
    #     url = reverse(SNIPPET_LIST)
    #     data = {'code': 'test5'}
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #
    # def test_partial_update_all_matches_put_NOT_ALLOWED_admin(self):
    #     """
    #     Ensure superuser cannot edit the list of matches object.
    #     """
    #     url = reverse(SNIPPET_LIST)
    #     data = {'code': 'test5'}
    #     self.client.login(username=self.admin.username, password=self.admin_plain_password)
    #     response = self.client.patch(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    #
    # def test_partial_update_all_matches_put_NOT_ALLOWED_user(self):
    #     """
    #     Ensure user cannot edit the list of matches object.
    #     """
    #     url = reverse(SNIPPET_LIST)
    #     data = {'code': 'test5'}
    #     self.client.login(username=self.user.username, password=self.user_plain_password)
    #     response = self.client.patch(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    #
    # def test_partial_update_all_matches_put_FORBIDDEN_unauthenficated(self):
    #     """
    #     Ensure unauthenticated user cannot edit the list of matches object.
    #     """
    #     url = reverse(SNIPPET_LIST)
    #     data = {'code': 'test5'}
    #     response = self.client.patch(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #
    # def test_create_match_OK_admin(self):
    #     """
    #     Ensure superuser can create a new match object.
    #     """
    #     url = reverse(SNIPPET_LIST)
    #     data = {'code': 'test6'}
    #     self.client.login(username=self.admin.username, password=self.admin_plain_password)
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    # def test_create_match_OK_user(self):
    #     """
    #     Ensure user can create a new match object.
    #     """
    #     url = reverse(SNIPPET_LIST)
    #     data = {'code': 'test7'}
    #     self.client.login(username=self.user.username, password=self.user_plain_password)
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    # def test_create_match_FORBIDDEN_unauthenficated(self):
    #     """
    #     Ensure unauthenticated user cannot create a new match object.
    #     """
    #     url = reverse(SNIPPET_LIST)
    #     data = {'code': 'test8'}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #
    # def test_get_match_test1_OK_admin(self):
    #     """
    #     Ensure superuser can view the match 'test1' object.
    #     """
    #     idTest1 = self.match1.id
    #     url = reverse(SNIPPET_DETAIL, args=[idTest1])
    #     self.client.login(username=self.admin.username, password=self.admin_plain_password)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_get_match_test1_user(self):
    #     """
    #     Ensure user can view the list of matchs object.
    #     """
    #     idTest1 = self.match1.id
    #     url = reverse(SNIPPET_DETAIL, args=[idTest1])
    #     self.client.login(username=self.user.username, password=self.user_plain_password)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_get_match_test1_unauthenficated(self):
    #     """
    #     Ensure unauthenticated user can view the list of match object.
    #     """
    #     idTest1 = self.match1.id
    #     url = reverse(SNIPPET_DETAIL, args=[idTest1])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_update_match_test1_OK_admin(self):
    #     """
    #     Ensure superuser update view the match created by him.
    #     """
    #     idTest1 = self.match2.id
    #     url = reverse(SNIPPET_DETAIL, args=[idTest1])
    #     data = {'code': 'test2 revu'}
    #     self.client.login(username=self.admin.username, password=self.admin_plain_password)
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Match.objects.get(id=idTest1).code, 'test2 revu')
    #
    # def test_update_match_test1_OK_user(self):
    #     """
    #     Ensure user update view the match created by him.
    #     """
    #     id_test = self.match1.id
    #     url = reverse(SNIPPET_DETAIL, args=[id_test])
    #     data = {'code': 'test1 revu'}
    #     self.client.login(username=self.user.username, password=self.user_plain_password)
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Match.objects.get(id=id_test).code, 'test1 revu')
    #
    # def test_update_match_test1_FORBIDDEN_unauthenficated(self):
    #     """
    #     Ensure unauthenficated user cannot update view the match.
    #     """
    #     id_test = self.match1.id
    #     url = reverse(SNIPPET_DETAIL, args=[id_test])
    #     data = {'code': 'test1 revu'}
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #
    # def test_update_match_test1_FORBIDDEN_admin(self):
    #     """
    #     Ensure superuser cannot update view the match created by other.
    #     """
    #     idTest1 = self.match1.id
    #     url = reverse(SNIPPET_DETAIL, args=[idTest1])
    #     data = {'code': 'test2 revu'}
    #     self.client.login(username=self.admin.username, password=self.admin_plain_password)
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #
    # def test_update_match_test1_FORBIDDEN_user(self):
    #     """
    #     Ensure user cannot update view the match created by other.
    #     """
    #     idTest1 = self.match2.id
    #     url = reverse(SNIPPET_DETAIL, args=[idTest1])
    #     data = {'code': 'test2 revu'}
    #     self.client.login(username=self.user.username, password=self.user_plain_password)
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #
    # def test_partial_update_match_test1_OK_admin(self):
    #     """
    #     Ensure superuser update view the match created by him.
    #     """
    #     idTest1 = self.match2.id
    #     url = reverse(SNIPPET_DETAIL, args=[idTest1])
    #     data = {'code': 'test2 revu'}
    #     self.client.login(username=self.admin.username, password=self.admin_plain_password)
    #     response = self.client.patch(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Match.objects.get(id=idTest1).code, 'test2 revu')
    #
    # def test_partial_update_match_test1_OK_user(self):
    #     """
    #     Ensure user update view the match created by him.
    #     """
    #     id_test = self.match1.id
    #     url = reverse(SNIPPET_DETAIL, args=[id_test])
    #     data = {'code': 'test1 revu'}
    #     self.client.login(username=self.user.username, password=self.user_plain_password)
    #     response = self.client.patch(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Match.objects.get(id=id_test).code, 'test1 revu')
    #
    # def test_partial_update_match_test1_FORBIDDEN_unauthenficated(self):
    #     """
    #     Ensure unauthenficated user cannot update view the match.
    #     """
    #     id_test = self.match1.id
    #     url = reverse(SNIPPET_DETAIL, args=[id_test])
    #     data = {'code': 'test1 revu'}
    #     response = self.client.patch(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #
    # def test_partial_update_match_test1_FORBIDDEN_admin(self):
    #     """
    #     Ensure superuser cannot update view the match created by other.
    #     """
    #     idTest1 = self.match1.id
    #     url = reverse(SNIPPET_DETAIL, args=[idTest1])
    #     data = {'code': 'test2 revu'}
    #     self.client.login(username=self.admin.username, password=self.admin_plain_password)
    #     response = self.client.patch(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #
    # def test_partial_update_match_test1_FORBIDDEN_user(self):
    #     """
    #     Ensure user cannot update view the match created by other.
    #     """
    #     idTest1 = self.match2.id
    #     url = reverse(SNIPPET_DETAIL, args=[idTest1])
    #     data = {'code': 'test2 revu'}
    #     self.client.login(username=self.user.username, password=self.user_plain_password)
    #     response = self.client.patch(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #
    # def test_get_match_highlight_test1_OK_admin(self):
    #     """
    #     Ensure superuser can view the match 'test1' highlight.
    #     """
    #     idTest1 = self.match1.id
    #     url = reverse(SNIPPET_HIGHLIGHT, args=[idTest1])
    #     self.client.login(username=self.admin.username, password=self.admin_plain_password)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_get_match_highlight_test1_OK_user(self):
    #     """
    #     Ensure superuser can view the match 'test1' highlight.
    #     """
    #     idTest1 = self.match1.id
    #     url = reverse(SNIPPET_HIGHLIGHT, args=[idTest1])
    #     self.client.login(username=self.user.username, password=self.user_plain_password)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_get_match_highlight_test1_OK_unauthenficated(self):
    #     """
    #     Ensure superuser can view the match 'test1' highlight.
    #     """
    #     idTest1 = self.match1.id
    #     url = reverse(SNIPPET_HIGHLIGHT, args=[idTest1])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)