# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Question(models.Model):

    """
    Class representing a question.
    """

    question_title = models.CharField(verbose_name=_('Title'), max_length=100,
                             null=False, blank=False)

    is_private = models.BooleanField(verbose_name=_('Is Private'),
            default=False)

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='questions')

class Answer(models.Model):

    """
    Class representing an answer.
    """

    answer_body = models.TextField(verbose_name=_('Answer'), null=False,
                            blank=False)

    question_id = models.ForeignKey(Question, related_name='answers')

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='given_answers')

class Tenant(models.Model):

    """
    Class representing a tenant.
    """

    tenant_name = models.CharField(verbose_name=_('Name'), max_length=50,
                            null=False, blank=False)

    api_key = models.CharField(verbose_name=_('Api Key'),
                               max_length=200, null=False, blank=False)

    def __unicode__(self):
        return self.name

class Request(models.Model):

    """
    Class representing an api request.
    """

    tenant = models.ForeignKey(Tenant, related_name='requests')

    url = models.CharField(verbose_name=_('Url'),
                               max_length=100, null=False, blank=False)

    requested_on = models.DateTimeField(default=timezone.now)

    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='requests')

