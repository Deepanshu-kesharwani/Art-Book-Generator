

import httpx
import os
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


async def chat_with_ai(messages):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": messages
    }

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(url, headers=headers, json=data)

        res = response.json()

        if "choices" not in res:
            raise Exception(f"OpenRouter Error: {res}")

        return res["choices"][0]["message"]["content"]

    except httpx.ReadTimeout:
        raise Exception("OpenRouter timeout (slow response)")

    except Exception as e:
        raise Exception(f"OpenRouter failed: {str(e)}")