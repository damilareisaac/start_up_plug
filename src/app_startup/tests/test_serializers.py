from django.test import TestCase, RequestFactory
import pytest
from app_startup.models import Tag
from app_startup.serializers import StartUpSerializer, TagSerializer
from django.utils.text import slugify

fake_request = RequestFactory().get("some_fake_endpoint")


@pytest.mark.django_db
class TestStartUpSerializer(TestCase):
    def setUp(self):
        self.maxDiff = None  # Set self.maxDiff to None

    def test_tag_create_serializer(self):
        data = {"name": "tag name", "slug": "tag-name"}
        s_tag = TagSerializer(data=data, context={"request": fake_request})
        TestCase.assertTrue(self, s_tag.is_valid())
        TestCase.assertEqual(self, s_tag.errors, {})
        TestCase.assertEqual(self, s_tag.validated_data, data)
        s_tag.save()
        TestCase.assertEqual(self, Tag.objects.count(), 1)
        tag_from_db = Tag.objects.get(name="tag name")
        TestCase.assertEqual(self, tag_from_db.name, data["name"])
        TestCase.assertEqual(self, tag_from_db.slug, data["slug"])

    def test_tag_update_serializer(self):
        old_name = "my tag"
        updated_name = "my updated tag"
        Tag.objects.create(name=old_name)
        tag, created = Tag.objects.get_or_create(
            name=old_name,
            defaults={"name": old_name},
        )
        TestCase.assertFalse(self, created)

        s_tag = TagSerializer(
            tag,
            data={"name": updated_name},
            partial=True,
            context={"request": fake_request},
        )
        TestCase.assertTrue(self, s_tag.is_valid())
        s_tag.save()
        tag_from_db = Tag.objects.filter(name=updated_name)

        TestCase.assertEqual(self, tag_from_db.count(), 1)
        TestCase.assertEqual(self, tag_from_db[0].name, updated_name)
        TestCase.assertEqual(self, tag_from_db[0].slug, slugify(old_name))

    @pytest.mark.skip
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
        TestCase.assertFalse(self, s_startup.is_valid())
        TestCase.assertEqual(self, s_startup.errors, {})
