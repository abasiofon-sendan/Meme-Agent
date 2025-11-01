from django.http import JsonResponse
from .views import fetch_meme
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def handle_a2a(request):
    try:
        meme = fetch_meme()
        return JsonResponse({
            "jsonrpc": "2.0",
            "id": 1,
            "result": {
                "text": f"Here's a programming meme for you 😄\n**{meme['title']}**",
                "blocks": [
                    {
                        "type": "image",
                        "image_url": meme["image_url"],
                        "alt_text": meme["title"]
                    },
                    {
                        "type": "section",
                        "text": f"[View on Reddit]({meme['postLink']})"
                    }
                ]
            }
        })
    except Exception as e:
        return JsonResponse({
            "jsonrpc": "2.0",
            "id": 1,
            "error": {"code": -32000, "message": str(e)}
        })
