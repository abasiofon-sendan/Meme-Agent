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

        # Unique IDs for the response
        task_id = str(uuid.uuid4())
        context_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        # Main message content
        message_text = (
            f"Here's a programming meme for you 🤖\n"
            f"**{meme['title']}**\n\n"
            f"[View on Reddit]({meme['postLink']})"
        )

        response_data = {
            "jsonrpc": "2.0",
            "id": task_id,
            "result": {
                "id": task_id,
                "contextId": context_id,
                "status": {
                    "state": "completed",
                    "timestamp": timestamp,
                    "message": {
                        "kind": "message",
                        "role": "agent",
                        "parts": [
                            {
                                "kind": "text",
                                "text": message_text
                            },
                            {
                                "kind": "file",   # ✅ changed back to "file"
                                "file_url": meme["image_url"],
                                "text": None
                            }
                        ],
                        "messageId": str(uuid.uuid4()),
                        "taskId": task_id
                    }
                },
                "artifacts": [
                    # {
                    #     "artifactId": str(uuid.uuid4()),
                    #     "name": "Meme Data",
                    #     "parts": [
                    #         {
                    #             "kind": "text",
                    #             "text": message_text
                    #         }
                    #     ]
                    # }
                ],
                "kind": "task"
            }
        }

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({
            "jsonrpc": "2.0",
            "error": {"code": -32000, "message": str(e)},
            "id": 1
        })
