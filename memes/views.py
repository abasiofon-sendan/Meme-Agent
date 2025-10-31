import requests
from django.http import JsonResponse

def fetch_meme():
    """Helper function to get a meme from external API"""
    response = requests.get("https://meme-api.com/gimme/ProgrammerHumor")
    response.raise_for_status()
    data = response.json()
    return {
        "title": data.get("title"),
        "image_url": data.get("url"),
        "postLink": data.get("postLink"),
    }
