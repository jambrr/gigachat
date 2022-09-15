from django.urls import re_path
from . import consumer

websocket_urlpatterns = [
    re_path(r'room/(?P<room_name>\w+)/$', consumer.ChatConsumer.as_asgi()),
]
