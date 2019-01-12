from django.db import close_old_connections
from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token


class TokenAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        try:
            access_token_name_index = scope['subprotocols'].index('access_token')
        except ValueError:
            raise ValueError('Authentication error: please, provide access_token header.')

        try:
            access_token = scope['subprotocols'][access_token_name_index + 1]
        except IndexError:
            raise ValueError('Authentication error: please, provide access_token.')

        try:
            token = Token.objects.get(key=access_token)
        except Token.DoesNotExist:
            raise ValueError('Authentication error: invalid token.')

        user = token.user
        close_old_connections()
        # Return the inner application directly and let it run everything else
        return self.inner(dict(scope, user=user))
