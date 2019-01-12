from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from ecg_handler import routing as ecg_routing
from .channels_authentication import TokenAuthMiddleware


application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': TokenAuthMiddleware(
        URLRouter(
            ecg_routing.websocket_urlpatterns
        )
    ),
})
