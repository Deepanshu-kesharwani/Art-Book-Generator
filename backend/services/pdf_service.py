

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
# from reportlab.platypus import SimpleDocTemplate, Image, Spacer, Paragraph, PageBreak
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.units import inch
# from PIL import Image as PILImage
# import os
#
#
# def create_pdf(image_paths, output_path, captions, title, width, height):
#
#     pdf = SimpleDocTemplate(
#         output_path,
#         pagesize=(width, height)  # ✅ match aspect ratio
#     )
#
#     styles = getSampleStyleSheet()
#     elements = []
#
#     # Title
#     elements.append(Paragraph(title, styles["Title"]))
#     elements.append(PageBreak())
#
#     temp_files = []
#
#     for i, path in enumerate(image_paths):
#
#         img = PILImage.open(path)
#         img = img.resize((width, height))
#
#         temp_path = path.replace(".png", "_temp.png")
#         img.save(temp_path)
#         temp_files.append(temp_path)
#
#         elements.append(Image(temp_path, width=width, height=height))
#         elements.append(Spacer(1, 10))
#
#         if i < len(captions):
#             elements.append(Paragraph(captions[i], styles["Normal"]))
#
#         if i < len(image_paths) - 1:
#             elements.append(PageBreak())
#
#     pdf.build(elements)
#
#     # ✅ cleanup temp files
#     for f in temp_files:
#         if os.path.exists(f):
#             os.remove(f)
# #




# from reportlab.platypus import SimpleDocTemplate, Image, Spacer, Paragraph, PageBreak
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.units import inch
# from PIL import Image as PILImage
# import os
#
#
# def create_pdf(image_paths, output_path, captions, title, width, height):
#
#     # Reduce page size slightly to avoid overflow
#     PAGE_WIDTH = width
#     PAGE_HEIGHT = height
#
#     pdf = SimpleDocTemplate(
#         output_path,
#         pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
#         rightMargin=20,
#         leftMargin=20,
#         topMargin=20,
#         bottomMargin=20
#     )
#
#     styles = getSampleStyleSheet()
#     elements = []
#
#     # Title page
#     elements.append(Paragraph(title, styles["Title"]))
#     elements.append(PageBreak())
#
#     MAX_WIDTH = PAGE_WIDTH - 40
#     MAX_HEIGHT = PAGE_HEIGHT - 40
#
#     temp_files = []
#
#     for i, path in enumerate(image_paths):
#
#         img = PILImage.open(path)
#         img_width, img_height = img.size
#
#         # 🔥 SCALE IMAGE TO FIT PAGE
#         ratio = min(MAX_WIDTH / img_width, MAX_HEIGHT / img_height)
#
#         new_width = int(img_width * ratio)
#         new_height = int(img_height * ratio)
#
#         resized = img.resize((new_width, new_height))
#
#         temp_path = path.replace(".png", "_temp.png")
#         resized.save(temp_path)
#         temp_files.append(temp_path)
#
#         elements.append(Image(temp_path, width=new_width, height=new_height))
#         elements.append(Spacer(1, 10))
#
#         if i < len(captions):
#             elements.append(Paragraph(captions[i], styles["Normal"]))
#
#         if i < len(image_paths) - 1:
#             elements.append(PageBreak())
#
#     pdf.build(elements)
#
#     # Cleanup temp files
#     for f in temp_files:
#         if os.path.exists(f):
#             os.remove(f)



#
# from reportlab.platypus import SimpleDocTemplate, Image, Spacer, Paragraph, PageBreak
# from reportlab.lib.styles import getSampleStyleSheet
# from PIL import Image as PILImage
# import os
#
#
# def create_pdf(image_paths, output_path, captions, title, width, height):
#
#     pdf = SimpleDocTemplate(
#         output_path,
#         pagesize=(width, height),
#         rightMargin=20,
#         leftMargin=20,
#         topMargin=20,
#         bottomMargin=20
#     )
#
#     styles = getSampleStyleSheet()
#     elements = []
#
#     # Title Page
#     elements.append(Paragraph(title, styles["Title"]))
#     elements.append(PageBreak())
#
#     MAX_WIDTH = width - 40
#     MAX_HEIGHT = height - 120  # 🔥 reserve space for caption
#
#     temp_files = []
#
#     for i, path in enumerate(image_paths):
#
#         img = PILImage.open(path)
#         img_width, img_height = img.size
#
#         # 🔥 SCALE IMAGE (leave space for caption)
#         ratio = min(MAX_WIDTH / img_width, MAX_HEIGHT / img_height)
#
#         new_width = int(img_width * ratio)
#         new_height = int(img_height * ratio)
#
#         temp_path = path.replace(".png", "_temp.png")
#         img.resize((new_width, new_height)).save(temp_path)
#         temp_files.append(temp_path)
#
#         # ✅ IMAGE
#         elements.append(Image(temp_path, width=new_width, height=new_height))
#         elements.append(Spacer(1, 12))
#
#         # ✅ CAPTION (same page, below image)
#         if i < len(captions):
#             elements.append(Paragraph(captions[i], styles["Normal"]))
#
#         # Next page
#         elements.append(PageBreak())
#
#     pdf.build(elements)
#
#     # Cleanup temp files
#     for f in temp_files:
#         if os.path.exists(f):
#             os.remove(f)