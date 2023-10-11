import pytest
from django.test import RequestFactory, TestCase

from app_startup.serializers import StartUpSerializer


@pytest.mark.django_db
class TestStartUpSerializer(TestCase):
    def test_start_up_serializer_with_no_tags(self):
        data = {
            "name": "StartUp name 1",
            "slug": "startup-name-1",
            "description": "StartUp description 1",
            "founded_date": "2015-12-10",
            "contact": "startup1@tech.com",
            "website": "http://startup1.tech.com",
        }
        fake_request = RequestFactory().get("some_fake_endpoint")
        s_startup = StartUpSerializer(
            data=data,
            context={"request": fake_request},
        )
        TestCase.assertTrue(self, s_startup.is_valid())
        TestCase.assertEqual(self, s_startup.errors, {})
        TestCase.assertDictEqual(self, s_startup.data, data)
