# import httpx, random

# async def get_programming_meme():
#     try:
#         async with httpx.AsyncClient() as client:
#             resp = await client.get("https://meme-api.com/gimme/ProgrammerHumor")
#             data = resp.json()
#             return {
#                 "text": data.get("title", "Here’s a programming meme 😂"),
#                 "image": data.get("url")
#             }
#     except Exception:
#         jokes = [
#             "Why do programmers prefer dark mode? — Because light attracts bugs!",
#             "There are 10 kinds of people in the world: those who understand binary and those who don’t.",
#             "I told my computer I needed a break — it said 'No problem, I’ll go to sleep.'"
#         ]
#         return {"text": random.choice(jokes), "image": None}
