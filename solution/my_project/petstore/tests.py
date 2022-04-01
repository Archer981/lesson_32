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
        application_info = response.data.get("paths").get("/api/petstore/{id}/").get('patch')

        self.assertTrue(
            application_info.get("description") == "Update application info",
            "Проверьте, что к эндпоинту /api/petstore/{id}/ (метод PATCH) описание соответствует заданию"
            f" (Update application info, тогда как у Вас - {application_info.get('description')})"
        )

        self.assertTrue(
            application_info.get("summary") == "Application update",
            "Проверьте, что к эндпоинту /api/dogs/ (метод GET) имеется пояснение Application update,"
            f" тогда как у Вас - {application_info.get('summary')}"
        )

    def test_swagger_page_is_active(self):
        response = self.client.get("/api/docs/")
        self.assertTrue(
            response.status_code == 200,
            "Проверьте, что страница с документацией по API доступна и открывается в браузере."
        )

