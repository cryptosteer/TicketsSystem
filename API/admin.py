from django.contrib import admin
from .models import Ticket, TicketPriority, TicketProblem, TicketStatus


admin.site.register(Ticket)
admin.site.register(TicketPriority)
admin.site.register(TicketProblem)
admin.site.register(TicketStatus)
