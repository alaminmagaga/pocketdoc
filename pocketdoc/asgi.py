"""
ASGI config for whatsapp_clone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pocketdoc.settings')
application = get_asgi_application()

import os
import django


from channels.routing import ProtocolTypeRouter, URLRouter,get_default_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pocketdoc.settings')
django.setup()
application = get_default_application()

from django.urls import path
from chats.consumers import PersonalChatConsumer

from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
        ])
    )
})
