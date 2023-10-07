from django.test import TestCase
import pytest
from collections import OrderedDict
from app_organizer.models import StartUp, Tag
from app_organizer.serializers import StartUpSerializer


@pytest.mark.django_db
class TestStartUpSerializer(TestCase):
    def setUp(self):
        self.maxDiff = None  # Set self.maxDiff to None

    @pytest.mark.skip
    def test_start_up_serializer(self):
        tag1, _ = Tag.objects.get_or_create(name="tag1")
        tag2, _ = Tag.objects.get_or_create(name="tag2")
        startup1 = StartUp.objects.create(
            name="StartUp name 1",
            description="StartUp description 1",
            founded_date="2015-12-10",
            contact="startup1@tech.com",
            website="http://startup1.tech.com",
        )
        startup1.tags.add(tag1, tag2)
        serialized_startup = StartUpSerializer(startup1)
        expected_tags = [
            OrderedDict({"name": "tag1", "slug": "tag1"}),
            OrderedDict({"name": "tag2", "slug": "tag2"}),
        ]
        expected_startup = {
            "id": 1,
            "name": "StartUp name 1",
            "slug": "startup-name-1",
            "description": "StartUp description 1",
            "founded_date": "2015-12-10",
            "contact": "startup1@tech.com",
            "website": "http://startup1.tech.com",
            "tags": expected_tags,
        }
        TestCase.assertDictEqual(self, expected_startup, serialized_startup.data)
