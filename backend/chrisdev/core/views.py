from django.http import HttpResponseRedirect
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ActivateUser(UserViewSet):
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())

        # Retrieve uid and token from request.GET
        uid = self.request.GET.get('uid')
        token = self.request.GET.get('token')

        # Pass uid and token to the serializer
        kwargs['data'] = {"uid": uid, "token": token}
        return serializer_class(*args, **kwargs)

    def activation(self, request, *args, **kwargs):
        super().activation(request, *args, **kwargs)

        return Response(status=status.HTTP_200_OK)

