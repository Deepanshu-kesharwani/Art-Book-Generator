


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import chat, generate
import os

app = FastAPI(title="Art Book Generator")

# ✅ serve outputs as public files
app.mount(
    "/outputs",
    StaticFiles(directory=os.path.abspath("outputs")),
    name="outputs"
)

app.include_router(chat.router, prefix="/chat")
app.include_router(generate.router, prefix="/generate")