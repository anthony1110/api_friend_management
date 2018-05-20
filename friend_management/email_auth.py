from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password


class UserModelEmailBackend(ModelBackend):
    __backend_path__ = 'friend_management.email_auth.UserModelEmailBackend'

    def authenticate(self, username="", password="", **kwargs):
        try:
            user = get_user_model().objects.get(email__iexact=username)
            if check_password(password, user.password):
                user.backend = UserModelEmailBackend.__backend_path__
                return user
            else:
                return None
        except get_user_model().DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None
