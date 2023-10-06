import pytest
import json

from django.test import TestCase
from django.db.utils import IntegrityError
from .models import Tag

# Create your tests here.


@pytest.mark.django_db
class TestTagModel(TestCase):
    @pytest.mark.parametrize("tag_name", "tag_slug", [("Isaac", "isaac")])
    def test_create_tag(self):
        print(self)
        # tag = Tag.objects.create(name=tag_name)
        # all_tag_names = Tag.objects.all().values_list(
        #     "name",
        #     "slug",
        #     flat=True,
        # )
        # TestCase.assertEqual(self, Tag.objects.count(), 1)
        # TestCase.assertEqual(self, tag.name, tag_name)
        # TestCase.assertEqual(self, tag.slug, tag_slug)
        # TestCase.assertIn(self, tag.name, all_tag_names)

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
