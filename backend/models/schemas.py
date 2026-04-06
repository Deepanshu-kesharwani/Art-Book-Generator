# from pydantic import BaseModel
#
# class ChatRequest(BaseModel):
#     message: str
#
# class GenerateRequest(BaseModel):
#     theme: str
#     num_pages: int
#     style: str
#     aspect_ratio: str



from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    message: str

class GenerateRequest(BaseModel):
    pages: List[str]
    style: str
    aspect_ratio: str
    title: str   # ✅ NEW