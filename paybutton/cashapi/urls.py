from django.urls import path, register_converter

from .converter import ApiKeyConverter

from . import views


app_name = 'cashapi'

urlpatterns = [
    path('<str:api_key>/', views.ProcessTransaction.as_view(), name='transact'),
    path('pay-with-card-checkout/', views.Checkout.as_view(),
         name='check-out'),
    path('pay-with-uuid/', views.UuidField.as_view(), name='uuid')
]