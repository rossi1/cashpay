from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import MerchantStore


class AuthenticateUser(BaseAuthentication):
    model = None

    def get_user_model(self):
        if self.model is not None:
            return self.model
        return MerchantStore

    def authenticate(self, request):
        model = self.get_user_model()

        try:
            user_field = request.session.get('username')
        except KeyError:
            raise exceptions.AuthenticationFailed('Invalid session Key')

        if 'username' not in request.session:
            raise exceptions.AuthenticationFailed('You are not authenticated')

        else:
            usr = model.token.get(usr__iexact=user_field)

            if usr:
                return usr, None
