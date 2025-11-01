import requests
from django.http import JsonResponse

def fetch_joke(request):
    """Fetch a random programming joke"""
    response = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
    response.raise_for_status()
    data = response.json()
    
    return JsonResponse({
        "joke": data.get("joke"),
        "category": data.get("category"),
    })
