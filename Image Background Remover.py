from rembg import remove
from PIL import Image

img = Image.open(r'C:\Users\alit9\Downloads\bird.jpg')
r = remove(img)
r.save(r'D:\Python Code\bird.png')
