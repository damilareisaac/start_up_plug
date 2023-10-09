from django.test import TestCase, Client, RequestFactory
import pytest


END_POINT = "/api/v1/blog/{}/"


@pytest.mark.django_db
class TestPostCreateAPI(TestCase):
    @pytest.mark.skip("not working yet")
    def test_post_create(self):
        request = RequestFactory()
        post_data = {
            "title": "Test to test what",
        }
        response = request.get(END_POINT.format("create"))
        TestCase.assertEqual(self, response.status_code, 201)
