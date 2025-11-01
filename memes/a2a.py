import uuid
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import requests


@csrf_exempt
@require_http_methods(["POST", "GET"])
def handle_a2a(request):
    try:
        # Fetch a programming joke from JokeAPI
        joke_response = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
        joke_response.raise_for_status()
        data = joke_response.json()
        joke_text = data.get("joke", "Here's a random programming joke for you!")

        # Generate unique IDs for message/task
        task_id = str(uuid.uuid4())
        context_id = str(uuid.uuid4())

        # Build the A2A-compatible JSON response
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
                                "text": f"😂 Here's a programming joke for you:\n\n{joke_text}"
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
