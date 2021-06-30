from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ffbbapi.models import Snippet,Match,Championship
from datetime import datetime


# Create your tests here.

class SnippetTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('testUser', 'test@test.com', 'test')
        Snippet.objects.create(code='test = "bar"\n', title='test1', owner=user)
        Snippet.objects.create(code='print("hello, world2")\n', title='test2', owner=user)

    def test_snippet_has_code(self):
        """Snippets that have code are correctly identified"""
        test1 = Snippet.objects.get(title="test1")
        test2 = Snippet.objects.get(title="test2")
        self.assertEqual(test1.code, 'test = "bar"\n')
        self.assertEqual(test2.code, 'print("hello, world2")\n')


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
        Ensure superuser can view the list of ffbbapi object.
        """
        url = reverse(SNIPPET_LIST)
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_snippets_OK_user(self):
        """
        Ensure user can view the list of ffbbapi object.
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
        Ensure superuser cannot edit the list of ffbbapi object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test5'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_all_snippets_put_NOT_ALLOWED_user(self):
        """
        Ensure user cannot edit the list of ffbbapi object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test5'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_all_snippets_put_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user cannot edit the list of ffbbapi object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test5'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_all_snippets_put_NOT_ALLOWED_admin(self):
        """
        Ensure superuser cannot edit the list of ffbbapi object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test5'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update_all_snippets_put_NOT_ALLOWED_user(self):
        """
        Ensure user cannot edit the list of ffbbapi object.
        """
        url = reverse(SNIPPET_LIST)
        data = {'code': 'test5'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update_all_snippets_put_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user cannot edit the list of ffbbapi object.
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
        id_test1 = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[id_test1])
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_snippet_test1_user(self):
        """
        Ensure user can view the list of ffbbapi object.
        """
        id_test1 = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[id_test1])
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_snippet_test1_unauthenficated(self):
        """
        Ensure unauthenticated user can view the list of snippet object.
        """
        id_test1 = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[id_test1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_snippet_test1_OK_admin(self):
        """
        Ensure superuser update view the snippet created by him.
        """
        id_test1 = self.snippet2.id
        url = reverse(SNIPPET_DETAIL, args=[id_test1])
        data = {'code': 'test2 revu'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Snippet.objects.get(id=id_test1).code, 'test2 revu')

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
        id_test1 = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[id_test1])
        data = {'code': 'test2 revu'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_snippet_test1_FORBIDDEN_user(self):
        """
        Ensure user cannot update view the snippet created by other.
        """
        id_test1 = self.snippet2.id
        url = reverse(SNIPPET_DETAIL, args=[id_test1])
        data = {'code': 'test2 revu'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_snippet_test1_OK_admin(self):
        """
        Ensure superuser update view the snippet created by him.
        """
        id_test1 = self.snippet2.id
        url = reverse(SNIPPET_DETAIL, args=[id_test1])
        data = {'code': 'test2 revu'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Snippet.objects.get(id=id_test1).code, 'test2 revu')

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
        id_test1 = self.snippet1.id
        url = reverse(SNIPPET_DETAIL, args=[id_test1])
        data = {'code': 'test2 revu'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_snippet_test1_FORBIDDEN_user(self):
        """
        Ensure user cannot update view the snippet created by other.
        """
        id_test1 = self.snippet2.id
        url = reverse(SNIPPET_DETAIL, args=[id_test1])
        data = {'code': 'test2 revu'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_snippet_highlight_test1_OK_admin(self):
        """
        Ensure superuser can view the snippet 'test1' highlight.
        """
        id_test1 = self.snippet1.id
        url = reverse(SNIPPET_HIGHLIGHT, args=[id_test1])
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_snippet_highlight_test1_OK_user(self):
        """
        Ensure superuser can view the snippet 'test1' highlight.
        """
        id_test1 = self.snippet1.id
        url = reverse(SNIPPET_HIGHLIGHT, args=[id_test1])
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_snippet_highlight_test1_OK_unauthenficated(self):
        """
        Ensure superuser can view the snippet 'test1' highlight.
        """
        id_test1 = self.snippet1.id
        url = reverse(SNIPPET_HIGHLIGHT, args=[id_test1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


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
        id_test1 = self.user.id
        url = reverse(USER_DETAIL, args=[id_test1])
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_FORBIDDEN_user(self):
        """
        Ensure user cannot view the list of users .
        """
        id_test1 = self.user.id
        url = reverse(USER_DETAIL, args=[id_test1])
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_user_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user can view the list of users object.
        """
        id_test1 = self.user.id
        url = reverse(USER_DETAIL, args=[id_test1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_user_put_NOT_ALLOWED_admin(self):
        """
        Ensure superuser cannot edit the list of users object.
        """
        id_test1 = self.user.id
        url = reverse(USER_DETAIL, args=[id_test1])
        data = {'username': 'testUser', 'email': 'test@test.com', 'password': 'test'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_put_NOT_ALLOWED_user(self):
        """
        Ensure user cannot edit the list of users object.
        """
        id_test1 = self.user.id
        url = reverse(USER_DETAIL, args=[id_test1])
        data = {'code': 'test5'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_user_put_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user cannot edit the list of users object.
        """
        id_test1 = self.user.id
        url = reverse(USER_DETAIL, args=[id_test1])
        data = {'code': 'test5'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


MATCH_LIST = 'match-list'
MATCH_DETAIL = 'match-detail'

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
        self.date1 = datetime(2020, 10, 4, 9, 45, 0, 0)
        self.date2 = datetime(2020, 12, 6, 20, 30, 0, 0)
        self.match1 = Match.objects.create(championship='b5e6211f1955b5e6212059fa2263', day=1,
                                           match_date=self.date1, home='ATLANTIQUE BC NAZAIRIEN',
                                           visitor='AS BRAINS BASKET',
                                           score_home=43, score_visitor=45, plan='533001012747', owner=self.user)
        self.match2 = Match.objects.create(championship='champ', day=3,
                                           match_date=self.date2, home='home',
                                           visitor='visiteur',
                                           score_home=43, score_visitor=45, plan='533001012778', owner=self.admin)


    def test_get_all_matches_OK_admin(self):
        """
        Ensure superuser can view the list of matches object.
        """
        url = reverse(MATCH_LIST)
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_matches_OK_user(self):
        """
        Ensure user can view the list of matches object.
        """
        url = reverse(MATCH_LIST)
        self.client.login(username=self.user.username, password=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_matches_OK_unauthenficated(self):
        """
        Ensure unauthenticated user can view the list of match object.
        """
        url = reverse(MATCH_LIST)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_all_matches_put_NOT_ALLOWED_admin(self):
        """
        Ensure superuser cannot edit the list of matches object.
        """
        url = reverse(MATCH_LIST)
        data = {'day': 4}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_all_matches_put_NOT_ALLOWED_user(self):
        """
        Ensure user cannot edit the list of matches object.
        """
        url = reverse(MATCH_LIST)
        data = {'day': 4}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_all_matches_put_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user cannot edit the list of matches object.
        """
        url = reverse(MATCH_LIST)
        data = {'day': 4}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_all_matches_put_NOT_ALLOWED_admin(self):
        """
        Ensure superuser cannot edit the list of matches object.
        """
        url = reverse(MATCH_LIST)
        data = {'day': 4}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update_all_matches_put_NOT_ALLOWED_user(self):
        """
        Ensure user cannot edit the list of matches object.
        """
        url = reverse(MATCH_LIST)
        data = {'day': 4}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update_all_matches_put_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user cannot edit the list of matches object.
        """
        url = reverse(MATCH_LIST)
        data = {'day': 4}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_match_OK_admin(self):
        """
        Ensure superuser can create a new match object.
        """
        url = reverse(MATCH_LIST)
        data = {'championship': 'champtest1', 'day': 5, 'match_date': self.date1, 'home': 'test_home',
                'visitor': 'test_visitor'}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_match_OK_user(self):
        """
        Ensure user can create a new match object.
        """
        url = reverse(MATCH_LIST)
        data = {'championship': 'champtest1', 'day': 5, 'match_date': self.date1, 'home': 'test_home',
                'visitor': 'test_visitor'}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_match_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenticated user cannot create a new match object.
        """
        url = reverse(MATCH_LIST)
        data = {'championship': 'champtest1', 'day': 5, 'match_date': self.date1, 'home': 'test_home',
                'visitor': 'test_visitor'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_match_test1_OK_admin(self):
        """
        Ensure superuser can view the match 'test1' object.
        """
        id_test1 = self.match1.id
        url = reverse(MATCH_DETAIL, args=[id_test1])
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_match_test1_user(self):
        """
        Ensure user can view the list of matchs object.
        """
        id_test1 = self.match1.id
        url = reverse(MATCH_DETAIL, args=[id_test1])
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_match_test1_unauthenficated(self):
        """
        Ensure unauthenticated user can view the list of match object.
        """
        id_test1 = self.match1.id
        url = reverse(MATCH_DETAIL, args=[id_test1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_match_test1_OK_admin(self):
        """
        Ensure superuser update view the match created by him.
        """
        id_test1 = self.match2.id
        url = reverse(MATCH_DETAIL, args=[id_test1])
        data = {'day': 3}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Match.objects.get(id=id_test1).day, 3)

    def test_partial_update_match_test1_OK_user(self):
        """
        Ensure user update view the match created by him.
        """
        id_test = self.match1.id
        url = reverse(MATCH_DETAIL, args=[id_test])
        data = {'day': 3}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Match.objects.get(id=id_test).day, 3)

    def test_partial_update_match_test1_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenficated user cannot update view the match.
        """
        id_test = self.match1.id
        url = reverse(MATCH_DETAIL, args=[id_test])
        data = {'day': 3}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_update_match_test1_OK_admin(self):
        """
        Ensure superuser update view the match created by him.
        """
        test1_id = self.match2.id
        test1_day = 3
        test1_championship = "b5e6211f1955b5e6212059fa2278"

        url = reverse(MATCH_DETAIL, args=[test1_id])
        data = {"championship": test1_championship, "day": test1_day, "match_date": "2020-10-11 10:30:00",
                "home": "testHome", "visitor": "AS BRAINS BASKET"}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Match.objects.get(id=test1_id).day, test1_day)
        self.assertEqual(Match.objects.get(id=test1_id).championship, test1_championship)

    def test_update_match_test1_OK_user(self):
        """
        Ensure user update view the match created by him.
        """
        test1_id = self.match1.id
        test1_day = 3
        test1_championship = "b5e6211f1955b5e6212059fa2278"
        url = reverse(MATCH_DETAIL, args=[test1_id])
        data = {"championship": test1_championship, "day": test1_day, "match_date": "2020-10-11 10:30:00",
                "home": "testHome", "visitor": "AS BRAINS BASKET"}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Match.objects.get(id=test1_id).day, test1_day)
        self.assertEqual(Match.objects.get(id=test1_id).championship, test1_championship)


    def test_update_match_test1_FORBIDDEN_unauthenficated(self):
        """
        Ensure unauthenficated user cannot update view the match.
        """
        test1_id = self.match1.id
        test1_day = 3
        test1_championship = "b5e6211f1955b5e6212059fa2278"
        url = reverse(MATCH_DETAIL, args=[test1_id])
        data = {"championship": test1_championship, "day": test1_day, "match_date": "2020-10-11 10:30:00",
                "home": "testHome", "visitor": "AS BRAINS BASKET"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_match_test1_FORBIDDEN_admin(self):
        """
        Ensure superuser cannot update view the match created by other.
        """
        test1_id = self.match1.id
        url = reverse(MATCH_DETAIL, args=[test1_id])
        data = {'day': 3}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_match_test1_FORBIDDEN_user(self):
        """
        Ensure user cannot update view the match created by other.
        """
        test1_id = self.match2.id
        url = reverse(MATCH_DETAIL, args=[test1_id])
        data = {'day': 3}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_match_test1_FORBIDDEN_admin(self):
        """
        Ensure superuser cannot update view the match created by other.
        """
        test1_id = self.match1.id
        url = reverse(MATCH_DETAIL, args=[test1_id])
        data = {'day': 3}
        self.client.login(username=self.admin.username, password=self.admin_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_match_test1_FORBIDDEN_user(self):
        """
        Ensure user cannot update view the match created by other.
        """
        test1_id = self.match2.id
        url = reverse(MATCH_DETAIL, args=[test1_id])
        data = {'day': 3}
        self.client.login(username=self.user.username, password=self.user_plain_password)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

