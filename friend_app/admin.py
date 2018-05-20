from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from friend_app import models
from friend_app.models import BlockedList, SubscribeList, Friend


class BlockedListAdmin(admin.ModelAdmin):
    model = BlockedList
    list_display = ["requestor", "target"]
    search_fields = ["requestor", "target"]
    list_filter = ["requestor", "target"]

admin.site.register(BlockedList, BlockedListAdmin)


class SubscribeListAdmin(admin.ModelAdmin):
    model = SubscribeList
    list_display = ["requestor", "target"]
    search_fields = ["requestor", "target"]
    list_filter = ["requestor", "target"]

admin.site.register(SubscribeList, SubscribeListAdmin)


class FriendAdmin(admin.ModelAdmin):
    model = Friend
    list_display = ["email1", "email2"]
    search_fields = ["email1", "email2"]
    list_filter = ["email1", "email2"]

admin.site.register(Friend, FriendAdmin)
