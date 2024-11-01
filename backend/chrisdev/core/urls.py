from django.urls import path

from backend.chrisdev.core.views import ActivateUser

urlpatterns = [
    path('activation/', ActivateUser.as_view({'get': 'activation'}), name='activation'),
]
