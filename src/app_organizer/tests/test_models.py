import pytest
import json

from django.test import TestCase
from django.db.utils import IntegrityError
from app_organizer.models import Tag, StartUp


# Create your tests here.
@pytest.mark.django_db
class TestStartUpModel(TestCase):
    def test_create_startup(self):
        some_tags = Tag.objects.bulk_create(
            [Tag(name=name) for name in ["technology", "fintech"]]
        )
        StartUp.objects.create(
            name="StartUp for tech name",
            description="StartUp for tech description",
            founded_date="2015-12-10",
            contact="tech@tech.com",
            website="http://tech.tech.com",
            tags=some_tags,
        )


@pytest.mark.django_db
class TestTagModel(TestCase):
    def test_create_tag(self):
        self.tag_name = "Tag 1"
        Tag.objects.create(name=self.tag_name)
        tag = Tag.objects.get(name=self.tag_name)
        TestCase.assertEqual(self, tag.name, "Tag 1")
        TestCase.assertEqual(self, tag.slug, "tag-1")

    def test_unique_constraints_on_tag_name_and_slug(self):
        Tag.objects.create(name="Isaac")
        with self.assertRaises(IntegrityError):
            Tag.objects.create(name="Isaac")

    def test_get_return_single_tag(self):
        Tag.objects.create(name="Isaac")
        Tag.objects.create(name="Damilare", slug="damilare")
        Tag.objects.create(name="Isaac3", slug="Isaac3")
        with self.assertRaises(Tag.MultipleObjectsReturned):
            Tag.objects.get(name__contains="Isaac")

    def test_bulk_create_tag(self):
        dummy_tag_names = ["Isaac", "Iyiola", "Ishola"]
        bulk_tags = Tag.objects.bulk_create(
            [Tag(name=name, slug=name.lower()) for name in dummy_tag_names]
        )
        TestCase.assertEqual(self, bulk_tags[0].slug, "isaac")
        TestCase.assertEqual(self, len(bulk_tags), len(dummy_tag_names))
