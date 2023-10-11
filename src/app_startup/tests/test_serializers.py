import pytest
from django.test import RequestFactory, TestCase
from app_startup.models import StartUp

from app_startup.serializers import StartUpSerializer
from app_tag.models import Tag

DATA = {
    "name": "StartUp name 1",
    "slug": "startup-name-1",
    "description": "StartUp description 1",
    "founded_date": "2015-12-10",
    "contact": "startup1@tech.com",
    "website": "http://startup1.tech.com",
    "tags": [],
}

FAKE_REQUEST = RequestFactory().get("some_fake_endpoint")


@pytest.mark.django_db
class TestStartUpSerializer(TestCase):
    def test_create_startup_with_no_tags(self):
        s_startup = StartUpSerializer(
            data=DATA,
            context={"request": FAKE_REQUEST},
        )
        TestCase.assertTrue(self, s_startup.is_valid())
        TestCase.assertEqual(self, s_startup.errors, {})
        saved_data = s_startup.save()
        TestCase.assertEqual(self, StartUp.objects.count(), 1)
        TestCase.assertEqual(self, saved_data.name, DATA["name"])

    def test_create_startup_with_tags(self):
        data = {
            **DATA,
            "tags": [
                {"name": "tag1"},
                {"name": "tag2"},
                {"name": "tag3"},
            ],
        }
        s_startup = StartUpSerializer(
            data=data,
            context={"request": FAKE_REQUEST},
        )
        TestCase.assertTrue(self, s_startup.is_valid())
        TestCase.assertEqual(self, s_startup.errors, {})
        TestCase.assertDictEqual(self, s_startup.data, data)

    def test_update_startup_with_no_tags(self):
        self.test_create_startup_with_no_tags()
        created_startup = StartUp.objects.get(name=DATA["name"])
        TestCase.assertCountEqual(self, created_startup.name, DATA["name"])
        created_startup.tags.add(Tag.objects.create(name="tag1", slug="tag1"))
        TestCase.assertEqual(self, created_startup.tags.count(), 1)
        updated_name = "Updated StartUp name"
        created_startup.name = updated_name
        created_startup.save()
        TestCase.assertEqual(
            self,
            StartUp.objects.get(name=updated_name).name,
            updated_name,
        )
