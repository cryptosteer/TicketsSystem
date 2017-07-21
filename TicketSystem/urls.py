from django.contrib import admin
from django.conf.urls import include, url
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('API.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^api/get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^', include('Client.urls')),
]
