from django.conf.urls import include, url
from .views import TicketViewSet, TicketPriorityViewSet, TicketProblemViewSet,\
    ticket_list, ticket_create, get_ticket, answer_ticket
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'ticket_priorities', TicketPriorityViewSet)
router.register(r'ticket_problems', TicketProblemViewSet)

urlpatterns = [
    url(r'^ticket_list/$', ticket_list, name='ticket_list'),
    url(r'^ticket_create/$', ticket_create, name='ticket_create'),
    url(r'^get_ticket/$', get_ticket, name='get_ticket'),
    url(r'^answer_ticket/$', answer_ticket, name='answer_ticket'),
    url(r'^', include(router.urls)),
]
