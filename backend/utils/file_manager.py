


import os
from datetime import datetime

# 🔥 absolute base dir (VERY IMPORTANT)
BASE_OUTPUT_DIR = os.path.abspath("outputs")


def ensure_base_dirs():
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)


def create_project_folder():
    """
    outputs/20260402_153210/
    """
    ensure_base_dirs()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    project_path = os.path.join(BASE_OUTPUT_DIR, timestamp)

    os.makedirs(os.path.join(project_path, "images"), exist_ok=True)
    os.makedirs(os.path.join(project_path, "book"), exist_ok=True)

    return project_path


def get_image_path(project_path, index):
    return os.path.join(project_path, "images", f"page_{index}.png")


def get_pdf_path(project_path):
    return os.path.join(project_path, "book", "artbook.pdf")