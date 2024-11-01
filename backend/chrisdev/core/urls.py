from django.urls import path

from .views import ActivateUser

urlpatterns = [
    path('activation/', ActivateUser.as_view({'get': 'activation'}), name='activation'),
]
