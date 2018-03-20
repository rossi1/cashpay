from django.urls import reverse_lazy

from rest_framework.views import APIView
from rest_framework import status, exceptions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializer import SerializerUser, SerializerToken
from .permission import UserPermission
from .authentication import AuthenticateUser
from .jt import Jwt
from .utils import request_url
from .models import MerchantStore, MerchantInfo


# noinspection PyUnusedLocal
class Index(APIView):
    authentication_classes = (AuthenticateUser,)
    """This is the default home view"""

    def get(self, request):

        """
        GET
        return a response to the logged in users
        """
        return Response({'current_logged_in as': request.user})


# noinspection PyUnusedLocal
class Login(APIView):
    """This view login users"""
    serializer_class = SerializerUser
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        POST:
        Param:
        usr : username
        pwd : passphrase

        Action: login users successfully and returns them to the home view

        """
        serial = self.serializer_class(data=request.data)

        if serial.is_valid(raise_exception=True):
            usr = serial.validated_data['usr']
            pwd = serial.validated_data['pwd']
            user = request_url(usr, pwd, request.user_agent.browser[0])
            if user.json().get('res'):
                get_user = user.json()['user']
                try:
                    merchant_data = MerchantStore.token.get(usr__iexact=get_user)
                except MerchantStore.DoesNotExist:
                    save_data = MerchantStore.token.create(usr=get_user)
                    save_data.save()
                    request.session['username'] = get_user
                    return Response({'detail': 'success', 'next_url': reverse_lazy('index')},
                                    status=status.HTTP_200_OK)
                else:
                    request.session['username'] = get_user
                    return Response({'detail': 'success', 'next_url': reverse_lazy('index')},
                                    status=status.HTTP_200_OK)

            elif user.status_code == 400:
                return Response({'detail': 'Invalid Credentails'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestToken(APIView):
    """This view generates tokens for users"""
    serializer_class = SerializerToken
    authentication_classes = (AuthenticateUser, )
    permission_classes = (UserPermission,)

    def post(self, request):
        """
        POST:

        param:
        url: the callback url
        returns: the api_key and token
        """

        serial = self.serializer_class(data=request.data)
        token = Jwt()
        create_token = token.encode_token(request.session['username'])
        if serial.is_valid(raise_exception=True):
            token_data = {'token': create_token.decode()}
            user = MerchantStore.token.get(usr=request.user)
            try:
                user_url = MerchantInfo.objects.get(merchant_id=user.pk)
            except MerchantInfo.DoesNotExist:
                save_url = MerchantInfo.objects.create(merchant_id=request.user)
                save_url.merchant_callback_url = serial.validated_data['url']
                save_url.save()
                return Response({'detail': serial.data, 'key': token_data}, status=status.HTTP_202_ACCEPTED)
            else:
                user_url.merchant_callback_url = serial.validated_data['url']
                user_url.save()
                return Response({'detail': serial.data, 'key': token_data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    """
    This view logs out authenticated users
    """
    authentication_classes = (AuthenticateUser,)
    permission_classes = (UserPermission,)

    def get(self, request):
        """
        Get:
        Log out the current user in the session.
        """
        try:
            request.session.flush()
        except KeyError:
            raise exceptions.NotFound('session key not found')
        else:
            message = 'You were successfully logged out'
            return Response({'message': message, 'url-to-login': reverse_lazy('login')},
                            status=status.HTTP_202_ACCEPTED)
