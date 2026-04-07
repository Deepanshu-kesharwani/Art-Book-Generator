

from fastapi import APIRouter, Request
from backend.models.schemas import ChatRequest
from backend.services.openrouter_service import chat_with_ai
import json

router = APIRouter()

memory = {}


@router.post("/")
async def chat(data: ChatRequest, request: Request):

    session_id = request.client.host

    if session_id not in memory:
        memory[session_id] = []

    system_prompt = """
You are Wizzy, an AI creative director.

IMPORTANT:
- ALWAYS return ONLY valid JSON
- NO text before or after JSON

FORMAT:
{
 "title": "book title",
 "style": "visual style",
 "pages": ["scene1", "scene2", ...]
}
"""

    memory[session_id].append({"role": "user", "content": data.message})

    messages = [{"role": "system", "content": system_prompt}] + memory[session_id]

    try:
        response = await chat_with_ai(messages)

        clean = response.strip().replace("```json", "").replace("```", "")
        parsed = json.loads(clean)

    except Exception as e:
        return {
            "error": "Chat failed",
            "details": str(e)
        }

    memory[session_id].append({"role": "assistant", "content": clean})

    return {"reply": parsed}



# from fastapi import APIRouter, Request
# from models.schemas import ChatRequest
# from services.openrouter_service import chat_with_ai
# import json
#
# router = APIRouter()
#
# memory = {}
#
#
# @router.post("/")
# async def chat(data: ChatRequest, request: Request):
#
#     session_id = request.client.host
#
#     if session_id not in memory:
#         memory[session_id] = []
#
#     system_prompt = """
# You are Wizzy, an expert AI creative director.
#
# GOAL:
# Help design a cohesive art book.
#
# RULES:
# - Suggest improvements to user ideas
# - Maintain narrative flow
# - Ensure visual consistency
#
# OUTPUT FORMAT (STRICT JSON):
# {
#  "title": "...",
#  "style": "...",
#  "pages": ["scene1", "scene2", ...]
# }
# """
#
#     memory[session_id].append({"role": "user", "content": data.message})
#
#     messages = [{"role": "system", "content": system_prompt}] + memory[session_id]
#
#     try:
#         response = await chat_with_ai(messages)
#
#         clean = response.strip().replace("```json", "").replace("```", "")
#         parsed = json.loads(clean)
#
#     except Exception as e:
#         return {
#             "error": "Invalid JSON from AI",
#             "raw": response
#         }
#
#     memory[session_id].append({"role": "assistant", "content": clean})
#
#     return {"reply": parsed}



