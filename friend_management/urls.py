from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from friend_management import settings
from . import views

urlpatterns = [
    # url(r'^$', views.Home, name='home'),
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^login$', views.enter, name='friend_management-login'),
    url(r'^admin/', admin.site.urls),
    url(r'^friend/', include('friend_app.urls')),
    url('^accounts/', include('django.contrib.auth.urls')),
]
