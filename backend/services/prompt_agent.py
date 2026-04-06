

from typing import List

def enhance_prompts(scenes: List[str], style: str) -> List[str]:
    """
    Convert user scenes into high-quality, consistent prompts
    """

    GLOBAL_STYLE = """
    cinematic lighting, ultra detailed, high quality, 4k,
    consistent color palette, same characters, same environment tone,
    visually cohesive art book style
    """

    prompts = []

    for scene in scenes:
        prompt = f"{scene}, {style}, {GLOBAL_STYLE}"
        prompts.append(prompt.strip())

    return prompts


#
# from typing import List, Dict
#
#
# def build_global_context(style: str) -> str:
#     return f"""
# GLOBAL ART DIRECTION:
# - Maintain SAME character across all scenes
# - Maintain SAME environment tone
# - Maintain SAME lighting conditions
# - Maintain SAME color palette
# - Cinematic composition, ultra detailed, 4k
#
# STYLE: {style}
#
# IMPORTANT:
# - Ensure visual continuity across all pages
# - Each image should feel like part of the SAME story
# """
#
#
# def enhance_prompts(scenes: List[str], style: str) -> List[str]:
#     """
#     Improved prompt engineering with global context + continuity
#     """
#
#     global_context = build_global_context(style)
#
#     prompts = []
#
#     for i, scene in enumerate(scenes):
#         prompt = f"""
# SCENE {i+1}:
# {scene}
#
# {global_context}
#
# Ensure consistency with previous scenes.
#         """
#         prompts.append(prompt.strip())
#
#     return prompts