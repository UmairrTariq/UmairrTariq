import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def img_to_text(path):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == '__main__':
    path = r'C:\Users\ma\Downloads\name1.jpg'
    extracted_txt = img_to_text(path)
    print('Extracted Text\n', extracted_txt)