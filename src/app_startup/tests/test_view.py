import pytest

from django.test import TestCase, Client


@pytest.mark.django_db
class TestStartUpView(TestCase):
    def test_start_up_get(self):
        client = Client()
