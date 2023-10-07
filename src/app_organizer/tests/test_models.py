import pytest
import datetime
from django.test import TestCase
from django.db.utils import IntegrityError
from app_organizer.models import Tag, StartUp


# Create your tests here.
@pytest.mark.django_db
class TestStartUpModel(TestCase):
    def test_create_startup(self):
        tag1, _ = Tag.objects.get_or_create(name="tag1")
        tag2, _ = Tag.objects.get_or_create(name="tag2")
        tag3, _ = Tag.objects.get_or_create(name="tag3")
        tag4, _ = Tag.objects.get_or_create(name="tag4")

        startup1 = StartUp.objects.create(
            name="StartUp name 1",
            description="StartUp description 1",
            founded_date="2015-12-10",
            contact="startup1@tech.com",
            website="http://startup1.tech.com",
        )
        startup2 = StartUp.objects.create(
            name="StartUp name 2",
            description="StartUp description 2",
            founded_date="2019-12-10",
            contact="startup2@tech.com",
            website="http://startup2.tech.com",
        )
        startup3 = StartUp.objects.create(
            name="StartUp name 3",
            description="StartUp description 3",
            founded_date="2014-01-01",
            contact="startup3@tech.com",
            website="http://startup3.tech.com",
        )
        startup1.tags.add(tag1, tag2)
        startup2.tags.add(tag3, tag2)
        startup3.tags.add(tag4, tag4, tag1)

    def test_startup_ordered_by_founded_date(self):
        self.test_create_startup()
        TestCase.assertEqual(
            self,
            StartUp.objects.first().founded_date,
            datetime.date(2019, 12, 10),
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
