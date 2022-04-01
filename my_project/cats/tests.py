from django.test import TestCase
from rest_framework.test import APIClient
from django.conf import settings

class SwaggerTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_swagger_file_is_active(self):
        self.assertTrue(
            'drf_spectacular' in settings.INSTALLED_APPS,
            "Проверьте, что добавили drf_spectacular в settings.py"
        )
        response = self.client.get("/api/")
        self.assertTrue(
            response.status_code == 200 and response.accepted_media_type == "application/vnd.oai.openapi",
            "Проверьте, что по адресу /api/ можно получить yaml-файл со схемой api проекта"
        )

    def test_swagger_page_is_active(self):
        response = self.client.get("/api/docs/")
        self.assertTrue(
            response.status_code == 200,
            "Проверьте, что страница с документацией по API доступна и открывается в браузере."
        )
