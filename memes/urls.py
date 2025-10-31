from django.urls import path
from .a2a import handle_a2a

urlpatterns = [
    path("a2a/meme/", handle_a2a, name="meme_agent"),
]
