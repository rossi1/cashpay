from django.core import signing
from rest_framework import permissions, authentication, \
    status, exceptions
from rest_framework.views import APIView


class ProcessTransaction(APIView):
    def post(self, request, api_key, **transact_data):
        get_api_key = request.QUERY_PARAMS.get(api_key)


class Checkout(APIView):
    def get(self, request):
        pass


class UuidField(APIView):
    def get(self, request):
        pass