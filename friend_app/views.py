#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python imports
import datetime
import re
import urllib

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http.response import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
from django.views.generic import View
from rest_framework.views import APIView

from friend_app import models
from friend_app.models import Friend, SubscribeList, BlockedList


# TODO: check valid email function
from friend_app.utils import get_valid_email


class AddFriendView(APIView):

    def post(self, request, *args, **kwargs):
        result = {"success": False, "message": "something wrong."}
        data = dict(request.data.items())

        if 'friends' in data:
            email_list = data.get('friends')
            if len(email_list) == 2:
                friend1 = get_valid_email(email_list[0])
                friend2 = get_valid_email(email_list[1])

                if friend2 and friend1:

                    if friend2.lower() != friend1.lower():    # two emails must be different

                        # check whether blocked or not.
                        if BlockedList.objects.filter(Q(requestor__iexact=friend1, target__iexact=friend2) | Q(requestor__iexact=friend2, target__iexact=friend1)).exists():
                            result = {"success": False, "message": "Blocked to being friend"}
                        else:
                            # add friend or already added
                            if (Friend.objects.filter(email1__iexact=friend1, email2__iexact=friend2).exists() or Friend.objects.filter(email1__iexact=friend2, email2__iexact=friend1).exists()):
                                result = {"success": False, "message": "Both are friends"}
                            else:
                                Friend(email1=friend1, email2=friend2).save()
                                result = {"success": True, "message": "successfully added."}
                else:
                    result = {"success": False, "message": "Need to provide 2 valid emails."}
            else:
                result = {"success": False, "message": "Need to provide 2 valid emails."}

        return JsonResponse(result)


class FriendListView(APIView):

    def post(self, request, *args, **kwargs):
        result = {"success": False, "message": "something wrong."}
        data = dict(request.data.items())

        if 'email' in data:
            target_email = get_valid_email(data.get('email'))
            if target_email:

                friend_list = Friend.get_friend_email_list(target_email)

                # if has blocked list then clear blocked list.
                blocked_list = [ blocked_obj.target for blocked_obj in BlockedList.objects.filter(Q(requestor__iexact=target_email))]

                for blocked_email in blocked_list:
                    if blocked_email in friend_list:
                        friend_list.remove(blocked_email)

                result = {"success": True,
                          "friends": friend_list,
                          "count": len(friend_list)}

        return JsonResponse(result)


class CommonFriendListView(APIView):

    def post(self, request, *args, **kwargs):
        result = {"success": False, "message": "something wrong."}
        data = dict(request.data.items())

        if 'friends' in data:
            email_list = data.get('friends')
            if len(email_list) == 2:
                friend_emails = data.get('friends')
                email1 = get_valid_email(friend_emails[0])
                email2 = get_valid_email(friend_emails[1])

                if email1 and email2:

                    friend_relationship1 = Friend.objects.filter(Q(email1__iexact=email1) | Q(email2__iexact=email1)).distinct()
                    friend_relationship2 = Friend.objects.filter(Q(email1__iexact=email2) | Q(email2__iexact=email2)).distinct()

                    friend_list1 = []
                    friend_list2 = []
                    for friend in friend_relationship1:
                        if friend.email1.lower() == email1.lower() and friend.email2.lower() != email1.lower():
                            friend_list1.append(friend.email2)
                        elif friend.email2.lower() == email1.lower() and friend.email1.lower() != email1.lower():
                            friend_list1.append(friend.email1)

                    for friend in friend_relationship2:
                        if friend.email1.lower() == email2.lower() and friend.email2.lower() != email2.lower():
                            friend_list2.append(friend.email2)
                        elif friend.email2.lower() == email2.lower() and friend.email1.lower() != email2.lower():
                            friend_list2.append(friend.email1)

                    common_list = []
                    for email in friend_list1:
                        if email in friend_list2:
                            common_list.append(email)
                    common_list = list(set(common_list))

                    result = {"success": True,
                              "friends": common_list,
                              "count": len(common_list)}
                else:
                    result = {"success": False, "message": "Need to provide 2 valid emails."}
            else:
                result = {"success": False, "message": "Need to provide 2 valid emails."}

        return JsonResponse(result)


class SubscribeUpdateView(APIView):

    def post(self, request, *args, **kwargs):
        result = {"success": False, "message": "something wrong."}
        data = dict(request.data.items())

        if 'requestor' in data and 'target' in data:
            requestor = get_valid_email(data.get('requestor'))
            target = get_valid_email(data.get('target'))

            if requestor and target:

                if requestor.lower() != target.lower():    # two emails must be different
                    if (SubscribeList.objects.filter(requestor__iexact=requestor, target__iexact=target).exists()):
                        result = {"success": False, "message": "already subscribed."}
                    else:
                        SubscribeList(requestor=requestor, target=target).save()
                        result = {"success": True, "message": "successfully subscribed."}
            else:
                result = {"success": False, "message": "Need to provide 2 valid emails."}

        return JsonResponse(result)


class BlockFriendView(APIView):

    def post(self, request, *args, **kwargs):
        result = {"success": False, "message": "something wrong."}
        data = dict(request.data.items())

        if 'requestor' in data and 'target' in data:
            requestor = get_valid_email(data.get('requestor'))
            target = get_valid_email(data.get('target'))

            if requestor and target:

                if requestor.lower() != target.lower():    # two emails must be different
                    if (BlockedList.objects.filter(requestor__iexact=requestor, target__iexact=target).exists()):
                        result = {"success": False, "message": "already blocked."}
                    else:
                        BlockedList(requestor=requestor, target=target).save()
                        result = {"success": True, "message": "successfully blocked."}

                    # remove from subscribe list
                    if SubscribeList.objects.filter(requestor__iexact=requestor, target__iexact=target).exists():
                        SubscribeList.objects.get(requestor__iexact=requestor, target__iexact=target).delete()
            else:
                result = {"success": False, "message": "Need to provide 2 valid emails."}

        return JsonResponse(result)


class SendMessageView(APIView):

    def post(self, request, *args, **kwargs):
        result = {"success": False, "message": "something wrong."}
        data = dict(request.data.items())

        if 'sender' in data and 'text' in data:
            sender = get_valid_email(data.get('sender'))
            text = data.get('text')

            if sender:

                # check for friends list
                recipient_list = Friend.get_friend_email_list(sender)

                # check for subscriber list
                subscriber_list = [subscribe_obj.target for subscribe_obj in SubscribeList.objects.filter(requestor__iexact=sender)]
                recipient_list.extend(subscriber_list)

                # check whether got mention in message text.
                email_list = re.findall(r'[\w\.-]+@[\w\.-]+', text)

                recipient_list.extend(email_list)

                # make unique recipient list.
                recipient_list = list(set(recipient_list))

                # check for blocked list
                blocked_list = [blocked_obj.target for blocked_obj in BlockedList.objects.filter(requestor__iexact=sender)]
                for blocked_email in blocked_list:
                    if blocked_email in recipient_list:
                        recipient_list.remove(blocked_email)

                result = {"success": True,
                          "recipients": recipient_list}
            else:
                result = {"success": False, "message": "Need to provide valid emails."}

        return JsonResponse(result)
