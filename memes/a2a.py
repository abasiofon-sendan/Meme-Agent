from pydantic import BaseModel, Field
from typing import Literal, Optional, List, Dict, Any
from uuid import uuid4
from datetime import datetime
from django.http import JsonResponse
from .views import fetch_meme


def handle_a2a(request):
    try:
        meme = fetch_meme()
        return JsonResponse({
            "jsonrpc": "2.0",
            "result": {
                "message": meme["title"],
                "image_url": meme["image_url"],
                "postLink": meme["postLink"]
            },
            "id": 1
        })
    except Exception as e:
        return JsonResponse({
            "jsonrpc": "2.0",
            "error": {"code": -32000, "message": str(e)},
            "id": 1
        })


    
