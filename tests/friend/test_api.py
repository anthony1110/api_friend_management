import json
import unittest
from django.test import Client

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from friend_app.models import Friend
from rest_framework.test import APIClient


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.client = APIClient()
        # initial some friends data

    def test_add_friend_api(self):

        post_data = json.dumps({"friends": ["andy@example.com", "john@example.com"]})

        response = self.client.post(reverse('add-friend'), data=post_data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = str(response.content, 'utf-8')
        result = json.loads(result)

        self.assertEqual(result.get("success"), True)
        self.assertEqual(result.get("message"), "successfully added.")

    def test_add_friend_api_with_wrong_email(self):

        post_data = json.dumps({"friends": ["andyexample.com", "john@example.com"]})

        response = self.client.post(reverse('add-friend'), data=post_data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = str(response.content, 'utf-8')
        result = json.loads(result)

        self.assertEqual(result.get("success"), False)
        self.assertEqual(result.get("message"), "Need to provide 2 valid emails.")

    def test_retrieve_friend_list_api(self):
        post_data = json.dumps({"email": "andy@example.com"})

        response = self.client.post(reverse('friend-list'), data=post_data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = str(response.content, 'utf-8')
        result = json.loads(result)

        self.assertEqual(result.get("success"), True)
        self.assertEqual(result.get("friends"), ["john@example.com", 'kahfai@example.com', 'kf@example.com'])
        self.assertEqual(result.get("count"), 3)

    def test_retrieve_common_friend_list_api(self):

        Friend(email1="kahfai@example.com", email2="andy@example.com").save()
        Friend(email1="kahfai@example.com", email2="john@example.com").save()
        Friend(email1="kf@example.com", email2="andy@example.com").save()
        Friend(email1="kf@example.com", email2="john@example.com").save()

        post_data = json.dumps({"friends": ["andy@example.com", "john@example.com"]})

        response = self.client.post(reverse('common-friend-list'), data=post_data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = str(response.content, 'utf-8')
        result = json.loads(result)

        self.assertEqual(result.get("success"), True)
        self.assertEqual(result.get("friends"), ["kahfai@example.com", "kf@example.com"])
        self.assertEqual(result.get("count"), 2)

    def test_subscribe_update_list_api(self):

        post_data = json.dumps({"requestor": "lisa@example.com", "target": "john@example.com"})

        response = self.client.post(reverse('subscribe-update-list'), data=post_data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = str(response.content, 'utf-8')
        result = json.loads(result)

        self.assertEqual(result.get("success"), True)
        self.assertEqual(result.get("message"), "successfully subscribed.")
