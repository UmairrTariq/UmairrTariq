from PIL import Image
img_path = r'C:\Users\ma\Downloads\pic.jpg'
img =Image.open(img_path)

bw_img = img.convert('L')

bw_img.save(r'C:\Users\ma\Downloads\pic1.jpg')

print("Image successfully converted to black and white")
