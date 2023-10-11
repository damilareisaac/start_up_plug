import pytest
import datetime
from django.test import TestCase
from app_startup.models import StartUp
from app_tag.models import Tag


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
