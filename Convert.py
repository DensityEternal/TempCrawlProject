from pdf2image import convert_from_path

# Specify the path to the PDF file
pdf_path = "path/to/your/pdf/file.pdf"

# Convert PDF to images
images = convert_from_path(pdf_path)

# Save each image as a separate file
for i, image in enumerate(images):
    image.save(f"output_{i}.jpg", "JPEG")