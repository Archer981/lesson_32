from django.test import TestCase
from rest_framework.test import APIClient


class SwaggerTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_swagger_file_is_active(self):
        response = self.client.get("/api/")
        self.assertTrue(
            response.status_code == 200 and response.accepted_media_type == "application/vnd.oai.openapi",
            "Проверьте, что по адресу /api/ можно получить yaml-файл со схемой api проекта"
        )

        dogs_info = response.data.get("paths").get("/api/dogs/").get('get')

        self.assertTrue(
            dogs_info.get("description") == "Retrieve dog list",
            "Проверьте, что к эндпоинту /api/dogs/ (метод GET) описание соответствует заданию (Retrieve dog list)"
        )

        self.assertTrue(
            dogs_info.get("summary") == "Dog list",
            "Проверьте, что к эндпоинту /api/dogs/ (метод GET) имеется пояснение Dog list"
        )

    def test_swagger_page_is_active(self):
        response = self.client.get("/api/docs/")
        self.assertTrue(
            response.status_code == 200,
            "Проверьте, что страница с документацией по API доступна и открывается в браузере."
        )

