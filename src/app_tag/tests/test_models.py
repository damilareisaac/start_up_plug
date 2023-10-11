from django.db import IntegrityError
from django.test import TestCase
import pytest

from app_tag.models import Tag


@pytest.mark.django_db
class TestTagModel(TestCase):
    def test_concrete_fields(self):
        fields_name = [field.name for field in Tag._meta.fields]
        expected_fields_name = ["id", "name", "slug"]
        TestCase.assertListEqual(
            self,
            fields_name,
            expected_fields_name,
        )

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
