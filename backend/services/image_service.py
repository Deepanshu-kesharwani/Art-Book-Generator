
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")


def generate_image(prompt, filename, width=1024, height=1024):
    """
    Generate image using HuggingFace SDXL API
    """

    url = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    # 🔥 truncate long prompts
    prompt = prompt[:500]

    payload = {
        "inputs": prompt,
        "parameters": {
            "width": width,
            "height": height
        }
    }

    for attempt in range(3):
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=60
            )

            if response.status_code == 200:
                with open(filename, "wb") as f:
                    f.write(response.content)
                return

            else:
                error_text = response.text
                print(f"❌ HF ERROR (attempt {attempt+1}): {error_text}")

                if "loading" in error_text.lower():
                    time.sleep(5)
                else:
                    time.sleep(2)

        except requests.exceptions.Timeout:
            print(f"⏳ Timeout on attempt {attempt+1}")
            time.sleep(3)

        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            time.sleep(2)

    raise Exception(f"Image generation failed after 3 attempts | Prompt: {prompt}")