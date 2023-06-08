from django.urls import path, include
from django.contrib import admin

from cats.urls import urlpatterns_cats
from dogs.urls import urlpatterns_dogs

# TODO настройте, пожалуйста здесь документацию drf_spectacular
# TODO а также подключите здесь urls имеющихся приложений
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatterns_cats)),
    path('', include(urlpatterns_dogs))
]
