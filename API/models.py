from django.db import models
from django.contrib.auth.models import User


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
    description = models.TextField("Describe Your Problem")
    status = models.ForeignKey(TicketStatus, verbose_name='Ticket status')
    assigned_to = models.ForeignKey(
        User, null=True, related_name='ticket_assigned_to',
        verbose_name='Assigend to')
    closed_date = models.DateTimeField("Closed", null=True, blank=True)

    def __str__(self):
        return self.problem.name + ': ' + self.description[0:40].strip()


class Serie(models.Model):

    HORROR = 'horror'
    COMEDY = 'comedy'
    ACTION = 'action'
    DRAMA = 'drama'

    CATEGORIES_CHOICES = (
        (HORROR, 'Horror'),
        (COMEDY, 'Comedy'),
        (ACTION, 'Action'),
        (DRAMA, 'Drama'),
    )

    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
