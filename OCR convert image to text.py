try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# needed to find tessseract program on computer (tesseract executable is not in PATH)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# simple interaction, put in image file name below to get output
print(pytesseract.image_to_string(Image.open('Untitled.png')))
