from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.views import generic

from friend_management.email_auth import UserModelEmailBackend


class Home(generic.TemplateView):
    template_name = 'home-clm.html'


def enter(request):
    logout(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        backend = UserModelEmailBackend()
        user = backend.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('contracts-list'))

    return HttpResponseRedirect('/')
