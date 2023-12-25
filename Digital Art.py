import numpy as np
import cv2

width,height = 800,600
image = np.zeros((height,width, 3), np.uint8)
image.fill(255)

# Create a Blue Sky.

sky_color = (255,255,0) #Blue
image[:int(height * 0.6), : ] = sky_color


# Create a Sun

sun_center = (150,150)
sun_radius = 50
sun_color = (0,255,255) # Yellow

cv2.circle(image,sun_center,sun_radius,sun_color, -1)

# Creating Mountains

mountain_color = (0,75,150) #Brown
cv2.fillPoly(image,[np.array([[0,400], [200,200] , [400,400]], np.int32)], mountain_color)
cv2.fillPoly(image,[np.array([[200,400], [400,200] , [600,400]], np.int32)], mountain_color)

# Createing Grass.

grass_color = (0 , 128,0) # green
cv2.rectangle(image,(0,int(height * 0.6)), (width,height), grass_color, -1 )

cv2.imshow('Nature Scene', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Save

cv2.imwrite(r'C:\Users\alit9\OneDrive\Desktop\Python Code\My Folder\nature_scene.jpg',image)

