

from reportlab.platypus import SimpleDocTemplate, Image, Spacer, Paragraph, PageBreak
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from PIL import Image as PILImage


def create_pdf(image_paths, output_path, captions, title):

    pdf = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []

    # Title Page
    elements.append(Paragraph(title, styles["Title"]))
    elements.append(PageBreak())

    PAGE_WIDTH, PAGE_HEIGHT = letter
    MAX_WIDTH = PAGE_WIDTH - 2 * inch
    MAX_HEIGHT = PAGE_HEIGHT - 2 * inch

    for i, path in enumerate(image_paths):

        img = PILImage.open(path)
        width, height = img.size

        ratio = min(MAX_WIDTH / width, MAX_HEIGHT / height)

        new_width = int(width * ratio)
        new_height = int(height * ratio)

        resized = img.resize((new_width, new_height))
        temp_path = path.replace(".png", "_resized.png")
        resized.save(temp_path)

        elements.append(Image(temp_path))
        elements.append(Spacer(1, 10))

        if i < len(captions):
            elements.append(Paragraph(captions[i], styles["Normal"]))

        # ✅ EACH IMAGE = NEW PAGE
        if i < len(image_paths) - 1:
            elements.append(PageBreak())

    pdf.build(elements)



#