import jwt
from datetime import timedelta
from django.conf import settings
from django.utils import timezone


class Jwt:
    algorithm = 'HS256'

    def encode_token(self, user_id, time_phrase=timedelta(weeks=5)):
        payload = {'sub':user_id,
                   'iat':timezone.now(),
                   'exp':timezone.now() + time_phrase
                   }
        return jwt.encode(payload, settings.SECRET_KEY, algorithm=self.algorithm)

    def decode_token(self, token):
        return jwt.decode(token, settings.SECRET_KEY, algorithm=self.algorithm)
