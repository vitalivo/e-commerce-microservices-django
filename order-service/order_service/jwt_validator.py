from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken
from django.contrib.auth.models import AnonymousUser


class NoUserValidationAccessToken(AccessToken):
    def verify(self):
        try:
            super().verify()
        except Exception:
            raise InvalidToken('Token is invalid or expired')

    def get_user(self):
        return AnonymousUser()