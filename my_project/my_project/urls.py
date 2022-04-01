from django.urls import path, include
from django.contrib import admin


# TODO настройте, пожалуйста здесь документацию drf_spectacular
# TODO а также подключите здесь urls имеющихся приложений
urlpatterns = [
    path('admin/', admin.site.urls),
]
