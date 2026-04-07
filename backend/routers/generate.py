


from fastapi import APIRouter
from backend.models.schemas import GenerateRequest
from backend.services.image_service import generate_image
from backend.services.pdf_service import create_pdf
from backend.services.prompt_agent import enhance_prompts
from backend.utils.file_manager import (
    create_project_folder,
    get_image_path,
    get_pdf_path
)

import os

router = APIRouter()


def get_dimensions(aspect_ratio):
    if aspect_ratio == "1:1":
        return (1024, 1024)
    elif aspect_ratio == "3:2":
        return (1200, 800)
    elif aspect_ratio == "2:3":
        return (800, 1200)
    elif aspect_ratio == "16:9":
        return (1280, 720)
    elif aspect_ratio == "9:16":
        return (720, 1280)
    else:
        return (1024, 1024)


@router.post("/")
def generate_book(data: GenerateRequest):

    try:
        project_path = create_project_folder()

        # ✅ Step 1: Prompt enhancement
        prompts = enhance_prompts(data.pages, data.style)
        title = data.title

        width, height = get_dimensions(data.aspect_ratio)

        image_paths = []

        # ✅ Step 2: Generate images (with debug logs)
        for i, prompt in enumerate(prompts):

            print(f"🎨 Generating image {i+1}/{len(prompts)}")

            path = get_image_path(project_path, i)

            try:
                generate_image(prompt, path, width, height)
            except Exception as e:
                print(f"❌ Error on image {i+1}: {e}")

                return {
                    "error": f"Image generation failed at page {i+1}",
                    "details": str(e)
                }

            image_paths.append(path)

        # ✅ Step 3: Create PDF
        pdf_path = get_pdf_path(project_path)
        create_pdf(image_paths, pdf_path, prompts, title)

        # ✅ Convert to URL paths
        def to_url(path):
            return path.replace(os.getcwd(), "").replace("\\", "/")

        return {
            "title": title,
            "images": [to_url(p) for p in image_paths],
            "pdf": to_url(pdf_path)
        }

    except Exception as e:
        print(f"🔥 BACKEND CRASH: {e}")

        return {
            "error": "Backend crashed",
            "details": str(e)
        }




#
# from fastapi import APIRouter
# from models.schemas import GenerateRequest
# from services.image_service import generate_image
# from services.pdf_service import create_pdf
# from services.prompt_agent import enhance_prompts
# from utils.file_manager import (
#     create_project_folder,
#     get_image_path,
#     get_pdf_path
# )
#
# import os
# from concurrent.futures import ThreadPoolExecutor, as_completed
# import zipfile
#
# router = APIRouter()
#
#
# def get_dimensions(aspect_ratio):
#     mapping = {
#         "1:1": (1024, 1024),
#         "3:2": (1200, 800),
#         "2:3": (800, 1200),
#         "16:9": (1280, 720),
#         "9:16": (720, 1280)
#     }
#     return mapping.get(aspect_ratio, (1024, 1024))
#
#
# @router.post("/")
# def generate_book(data: GenerateRequest):
#
#     try:
#         project_path = create_project_folder()
#
#         prompts = enhance_prompts(data.pages, data.style)
#         title = data.title
#
#         width, height = get_dimensions(data.aspect_ratio)
#
#         image_paths = [get_image_path(project_path, i) for i in range(len(prompts))]
#
#         # 🔥 PARALLEL IMAGE GENERATION
#         def worker(prompt, path):
#             try:
#                 generate_image(prompt, path, width, height)
#                 return path
#             except Exception as e:
#                 print(f"❌ Failed: {e}")
#                 return None
#
#         results = []
#         with ThreadPoolExecutor(max_workers=4) as executor:
#             futures = [
#                 executor.submit(worker, p, path)
#                 for p, path in zip(prompts, image_paths)
#             ]
#
#             for f in as_completed(futures):
#                 results.append(f.result())
#
#         # Remove failed images
#         image_paths = [r for r in results if r is not None]
#
#         if not image_paths:
#             return {"error": "All image generations failed"}
#
#         # ✅ PDF
#         pdf_path = get_pdf_path(project_path)
#         create_pdf(image_paths, pdf_path, prompts, title, width, height)
#
#         # ✅ ZIP images
#         zip_path = os.path.join(project_path, "images.zip")
#         with zipfile.ZipFile(zip_path, 'w') as z:
#             for img in image_paths:
#                 z.write(img, os.path.basename(img))
#
#         def to_url(path):
#             return path.replace(os.getcwd(), "").replace("\\", "/")
#
#         return {
#             "title": title,
#             "images": [to_url(p) for p in image_paths],
#             "pdf": to_url(pdf_path),
#             "zip": to_url(zip_path)
#         }
#
#     except Exception as e:
#         return {"error": str(e)}