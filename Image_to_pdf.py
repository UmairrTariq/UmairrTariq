from PIL import Image

img_path = r'C:\Users\ma\Downloads\img.png'
img = Image.open(img_path)

if img.mode != 'RGB':
    img = img.convert("RGB")

pdf_path = r'C:\Users\ma\Downloads\img.pdf'
img.save(pdf_path)

print('Image successfully Converted to PDF')
