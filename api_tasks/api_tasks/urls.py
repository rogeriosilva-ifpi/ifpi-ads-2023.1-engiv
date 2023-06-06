from django.contrib import admin
from django.urls import include, path

from tasks import urls as tasks_urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include(tasks_urls.urlspatterns)),
    path('core/', include('core.urls')),
]
