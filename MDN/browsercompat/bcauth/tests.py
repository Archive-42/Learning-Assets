# -*- coding: utf-8 -*-
"""Tests for bcauth."""

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
import mock

from webplatformcompat.tests.base import TestCase
from .templatetags.helpers import providers_media_js, provider_login_url


class TestViews(TestCase):
    def full_reverse(self, viewname):
        """Create a full URL for a view."""
        return 'http://testserver' + reverse(viewname)

    def test_account_anon(self):
        response = self.client.get(reverse('account_base'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['Location'], self.full_reverse('account_login'))

    def test_account_logged_in(self):
        self.login_user()
        response = self.client.get(reverse('account_base'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['Location'], self.full_reverse('account_profile'))

    def test_profile_anon(self):
        url = reverse('account_profile')
        response = self.client.get(reverse('account_profile'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['Location'],
            self.full_reverse('account_login') + '?next=' + url)

    def test_profile_logged_in(self):
        user = self.login_user()
        user.emailaddress_set.create(email=user.email)
        response = self.client.get(reverse('account_profile'))
        self.assertEqual(response.status_code, 200)


class TestProvidersMediaJS(TestCase):
    def setUp(self):
        self.patcher = mock.patch(
            'bcauth.templatetags.helpers.providers.registry.get_list')
        self.mocked_get_list = self.patcher.start()
        self.addCleanup(self.patcher.stop)
        self.context = {'request': 'fake request'}

    def test_empty(self):
        self.mocked_get_list.return_value = []
        actual = providers_media_js(self.context)
        self.assertEqual('', actual)

    def test_provider(self):
        mock_provider = mock.Mock(spec_set=['media_js'])
        fake_js = '<script>some.JS();</script>'
        mock_provider.media_js.return_value = fake_js
        self.mocked_get_list.return_value = [mock_provider]
        actual = providers_media_js(self.context)
        self.assertEqual(fake_js, actual)
        mock_provider.media_js.assert_called_once_with(self.context['request'])


class TestProviderLoginUrl(TestCase):
    def setUp(self):
        self.patcher = mock.patch(
            'bcauth.templatetags.helpers.providers.registry.by_id')
        self.mocked_by_id = self.patcher.start()
        self.addCleanup(self.patcher.stop)
        self.context = {'request': 'fake request'}
        self.provider = mock.Mock(spec_set=['get_login_url'])
        self.fake_url = 'http://example.com/AUTH'
        self.provider.get_login_url.return_value = self.fake_url
        self.mocked_by_id.return_value = self.provider

        self.request = mock.Mock(spec_set=['POST', 'GET', 'get_full_path'])
        self.request.POST = {}
        self.request.GET = {}
        self.request.get_full_path.side_effect = Exception('Not Called')

    def test_basic(self):
        actual = provider_login_url(self.request, 'provider', 'process')
        self.assertEqual(actual, self.fake_url)
        self.provider.get_login_url.assert_called_once_with(
            self.request, process='process')

    def test_scope(self):
        actual = provider_login_url(
            self.request, 'provider', 'process', scope='SCOPE')
        self.assertEqual(actual, self.fake_url)
        self.provider.get_login_url.assert_called_once_with(
            self.request, process='process', scope='SCOPE')

    def test_auth_params(self):
        actual = provider_login_url(
            self.request, 'provider', 'process', auth_params={'foo': 'BAR'})
        self.assertEqual(actual, self.fake_url)
        self.provider.get_login_url.assert_called_once_with(
            self.request, process='process', auth_params={'foo': 'BAR'})

    def test_explicit_next(self):
        actual = provider_login_url(
            self.request, 'provider', 'process', next='/next')
        self.assertEqual(actual, self.fake_url)
        self.provider.get_login_url.assert_called_once_with(
            self.request, process='process', next='/next')

    def test_post_next(self):
        self.request.POST['next'] = '/post'
        self.request.GET['next'] = '/get'
        actual = provider_login_url(self.request, 'provider', 'process')
        self.assertEqual(actual, self.fake_url)
        self.provider.get_login_url.assert_called_once_with(
            self.request, process='process', next='/post')

    def test_get_next(self):
        self.request.GET['next'] = '/get'
        actual = provider_login_url(self.request, 'provider', 'process')
        self.assertEqual(actual, self.fake_url)
        self.provider.get_login_url.assert_called_once_with(
            self.request, process='process', next='/get')

    def test_redirect_next(self):
        self.request.get_full_path.side_effect = None
        self.request.get_full_path.return_value = 'http://example.com/full'
        actual = provider_login_url(self.request, 'provider', 'redirect')
        self.assertEqual(actual, self.fake_url)
        self.provider.get_login_url.assert_called_once_with(
            self.request, process='redirect', next='http://example.com/full')
