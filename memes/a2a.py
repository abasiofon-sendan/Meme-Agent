import uuid
from django.http import JsonResponse
from .views import fetch_meme
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["POST", "GET"])
def handle_a2a(request):
    try:
        meme = fetch_meme()

        # generate unique IDs for message/task
        task_id = str(uuid.uuid4())
        context_id = str(uuid.uuid4())

        response_data = {
            "jsonrpc": "2.0",
            "id": 1,
            "result": {
                "id": task_id,
                "contextId": context_id,
                "status": {
                    "state": "completed",
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                    "message": {
                        "kind": "message",
                        "role": "agent",
                        "parts": [
                            {
                                "kind": "text",
                                "text": f"Here's a programming meme for you 🤖\n**{meme['title']}**"
                            },
                            {
                                "kind": "image",
                                "file_url": meme["image_url"],
                                "text": None
                            },
                            {
                                "kind": "text",
                                "text": f"[View on Reddit]({meme['postLink']})"
                            }
                        ],
                        "messageId": str(uuid.uuid4()),
                        "taskId": task_id
                    }
                },
                "artifacts": []
            }
        }

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({
            "jsonrpc": "2.0",
            "error": {"code": -32000, "message": str(e)},
            "id": 1
        })