# 🎨 Art Book Generator

An AI-powered system that generates complete visual storybooks using Large Language Models (LLMs) and diffusion-based image generation.

---

## 🚀 Features

- ✨ AI-driven story generation (OpenRouter)
- 🎯 Prompt enhancement for visual consistency
- 🖼️ Image generation using Stable Diffusion (HuggingFace)
- 📄 Automatic PDF art book creation
- 🎨 Interactive UI with Streamlit
- 📂 Downloadable art book (images + PDF)

---

## 🧱 Architecture

Frontend (Streamlit) → Backend (FastAPI) → External APIs

### 🔹 Backend (FastAPI)
- Handles AI chat generation
- Enhances prompts for consistency
- Generates images using HuggingFace
- Creates final PDF using ReportLab
- Serves generated outputs

### 🔹 Frontend (Streamlit)
- Chat interface for idea generation
- Scene editor for customization
- Displays generated images
- Provides PDF download

---

## ⚙️ Tech Stack

- **Backend:** FastAPI, Python  
- **Frontend:** Streamlit  
- **AI APIs:** OpenRouter, HuggingFace Inference API  
- **PDF Generation:** ReportLab  
- **Containerization:** Docker & Docker Compose  

---

## 📁 Project Structure

```
ArtBookGenerator/
│
├── backend/
│   ├── main.py
│   ├── models/
│   │   └── schemas.py
│   ├── outputs/   
│   ├── routers/
│   │   ├── chat.py
│   │   └── generate.py
│   ├── services/
│   │   ├── image_service.py
│   │   ├── openrouter_service.py
│   │   ├── pdf_service.py
│   │   └── prompt_agent.py
│   └── utils/
│       └── file_manager.py
│
├── frontend/
│   └── app.py
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
│
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md

```

---

## 🐳 Run with Docker

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ArtBookGenerator
```

---

### 2. Setup environment variables

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```env
HF_API_KEY=your_huggingface_key
OPENROUTER_API_KEY=your_openrouter_key
```

---

### 3. Run the application

```bash
docker-compose up --build
```

---

### 4. Open in browser

```text
http://localhost:7860
```

---

## 📂 Output

Generated files are stored in:

```text
outputs/{timestamp}/
```

Includes:

- 🖼️ Generated images
- 📄 Final PDF art book

---

## ⚠️ Important Notes

- Do NOT commit `.env` (contains API keys)
- Ensure Docker is installed and running
- Backend runs internally on port `8000`
- Frontend runs on port `7860`

---

## 📌 Future Improvements

- ⚡ Async image generation (parallel processing)
- 🧠 Task queue (Celery + Redis)
- 🗄️ Database for session persistence
- 🔐 Authentication system
- 🌐 Deployment with domain + HTTPS

---

## 🚀 Deployment (VPS - Docker)

```bash
git clone <your-repo-url>
cd ArtBookGenerator

cp .env.example .env
# add your API keys

docker-compose up --build -d
```

Access:

```text
http://your-vps-ip:7860
```

---

## 🧠 Key Learnings

- Multi-service architecture using Docker
- Integration of LLM + Diffusion models
- Prompt engineering for visual consistency
- Backend-Frontend communication in containers
- Handling long-running AI tasks

---

## 👨‍💻 Author

**Deepanshu Kesharwani**  
B.Tech CSE | AI/ML Enthusiast

---

