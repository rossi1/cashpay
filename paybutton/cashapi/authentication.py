import jwt
from rest_framework.authentication import BaseAuthentication, \
    get_authorization_header
from rest_framework import exceptions
from .jt import Jwt

from ..tokenapi.models import MerchantStore


class AuthenticateToken(BaseAuthentication):
    model = None

    def get_model(self):
        if self.model is not None:
            return self.model
        else:
            return MerchantStore

    def authenticate(self, request):
        """
        This method overides the authenticate method
        :param request:
        :return: it takes the decoded token and return it to
        the authenticate_credential method
        """
        token = Jwt()
        auth = get_authorization_header(request).split()[1]

        if auth:
            try:
                resp = token.decode_token(auth)
            except jwt.ExpiredSignatureError:
                raise exceptions.AuthenticationFailed('Token expired')
            except jwt.InvalidTokenError:
                raise exceptions.AuthenticationFailed('Token provided is invalid')
            else:
                return self.authenticate_credentials(resp['sub'])

    def authenticate_credentials(self, user):
        model = self.get_model()
        try:
            usr = model.tokens.get(usr__iexact=user)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid credential')
        else:
            return usr, None

    def authenticate_header(self, request):
        """
        This method overrides the request header
        """
        pass
