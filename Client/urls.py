from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.customer),
    url(r'^agent/$', views.agent),
]
