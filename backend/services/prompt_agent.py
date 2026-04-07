

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