from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken
from django.contrib.auth.models import AnonymousUser

class NoUserValidationAccessToken(AccessToken):
    def verify(self):
        # Проверяем только подпись, не пытаемся загрузить пользователя
        try:
            super().verify()
        except Exception:
            raise InvalidToken('Token is invalid or expired')
    
    def get_user(self):
        # Не пытаемся получить пользователя из БД
        return AnonymousUser()  # или создай легковесного юзера