from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class TicketPriority(models.Model):

    class Meta:
        verbose_name_plural = 'Ticket priorities'
        ordering = ["order"]

    name = models.CharField(max_length=50)
    value = models.CharField(max_length=20)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class TicketProblem(models.Model):

    class Meta:
        ordering = ["order"]

    name = models.CharField(max_length=50)
    value = models.CharField(max_length=20)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class TicketStatus(models.Model):

    class Meta:
        verbose_name_plural = 'Ticket statuses'
        ordering = ["order"]

    name = models.CharField(max_length=50)
    value = models.CharField(max_length=20)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):

    created_by = models.ForeignKey(
        User, related_name='ticket_created_by', verbose_name='Created by')
    created_date = models.DateTimeField("Created date", auto_now_add=True)
    order_number = models.CharField("Order reference No", max_length=50)
    priority = models.ForeignKey(TicketPriority, verbose_name='Ticket priority')
    problem = models.ForeignKey(
        TicketProblem, verbose_name='I\'m having a problem with')
    description = models.TextField("Describe your problem")
    status = models.ForeignKey(
        TicketStatus, verbose_name='Ticket status', default=1)
    assigned_to = models.ForeignKey(
        User, related_name='ticket_assigned_to', verbose_name='Assigend to',
        null=True, blank=True)
    closed_date = models.DateTimeField("Closed", null=True, blank=True)

    def __str__(self):
        return self.problem.name + ': ' + self.description[0:40].strip()


class TicketItem():

    def __init__(self, id, order, created, closed, created_by, priority, problem, description, status, agent):
        self.id = id
        self.order = order
        self.created = created
        self.closed = closed
        self.created_by = created_by
        self.priority = priority
        self.problem = problem
        self.description = description
        self.status = status
        self.agent = agent
