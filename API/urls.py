from django.conf.urls import include, url
from .views import SerieViewSet, TicketViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'series', SerieViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
