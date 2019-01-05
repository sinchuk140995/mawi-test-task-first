from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
# from django.contrib.auth.models import User


class Home(APIView):
    """
    Home test view.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """
        Return a 'Hello, World!'.
        """
        return Response('Hello, World!!!')
