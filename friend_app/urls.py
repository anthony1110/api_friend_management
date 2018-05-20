from django.conf.urls import url

from friend_app import views

urlpatterns = [
    url(r'^add_friend', views.AddFriendView.as_view(), name='add-friend'),
    url(r'^friend_list', views.FriendListView.as_view(), name='friend-list'),
    url(r'^common_friend_list', views.CommonFriendListView.as_view(), name='common-friend-list'),
    url(r'^subscribe_update', views.SubscribeUpdateView.as_view(), name='subscribe-update-list'),
    url(r'^block_friend', views.BlockFriendView.as_view(), name='block-friend'),
    url(r'^send_message', views.SendMessageView.as_view(), name='send-message'),
]
