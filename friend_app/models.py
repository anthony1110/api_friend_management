# Python imports
from __future__ import absolute_import, unicode_literals

import os
import uuid
import datetime
import logging
from decimal import Decimal

import pytz
from bulk_update.manager import BulkUpdateManager
from django.conf import settings
from django.contrib.auth.models import Group, User
from django.db import models
from django.db.models import Q
from django_bulk_update.helper import bulk_update


logger = logging.getLogger('django')

class BlockedList(models.Model):
    requestor = models.EmailField()
    target = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = ('requestor', 'target',)

class SubscribeList(models.Model):
    requestor = models.EmailField()
    target = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = ('requestor', 'target',)

class Friend(models.Model):
    email1 = models.EmailField()
    email2 = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = ('email1', 'email2',)

    @classmethod
    def get_friend_email_list(cls, target_email):
        friend_list = []

        if target_email:
            friend_relationship1 = Friend.objects.filter(Q(email1__iexact=target_email) | Q(email2__iexact=target_email)).distinct()

            for friend in friend_relationship1:
                if friend.email1.lower() == target_email.lower() and friend.email2.lower() != target_email.lower():
                    friend_list.append(friend.email2)
                elif friend.email2.lower() == target_email.lower() and friend.email1.lower() != target_email.lower():
                    friend_list.append(friend.email1)

        return friend_list


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile')

    def __str__(self):
        return self.user.username