from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('API.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('Client.urls')),
]
