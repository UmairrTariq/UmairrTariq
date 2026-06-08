import cv2
import os
import numpy as np

def cartoonize_image(img):
    # 1. Heavily smooth the image using bilateral filtering to remove skin texture/stubble
    # Running multiple small passes yields a much cleaner "vector art" look than one big pass
    smoothed = img.copy()
    for _ in range(3):
        smoothed = cv2.bilateralFilter(smoothed, d=9, sigmaColor=30, sigmaSpace=30)
        
    # 2. Quantize colors (K-Means or Division) to create flat color blocks
    # This removes gradients and gives it an intentional, clean graphic style
    div = 32  # Increase this (e.g., 64) for fewer, flatter colors
    quantized = (smoothed // div) * div + (div // 2)
    
    # 3. Add soft, subtle contours instead of harsh black ink lines
    # We use a gentle blur mask to only ink major transitions (like head vs background)
    gray = cv2.cvtColor(smoothed, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, blockSize=15, C=4
    )
    
    # Combine the clean flat colors with the gentle edges
    cartoon = cv2.bitwise_and(quantized, quantized, mask=edges)
    return cartoon


def bulk_process(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"cartoon_{filename}")
            
            try:
                img = cv2.imread(input_path)
                if img is None:
                    print(f"Skipped (unreadable): {filename}")
                    continue
                
                print(f"Processing: {filename}...")
                result = cartoonize_image(img)
                
                cv2.imwrite(output_path, result)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print(f"\nDone! Check the '{output_folder}' folder.")

# --- CONFIGURATION ---
# Change these folder names if you like
INPUT_DIR = r"C:\Users\ma\Desktop\Python Code\raw_images"
OUTPUT_DIR = r"C:\Users\ma\Desktop\Python Code\images_output"

# Create input folder automatically if it doesn't exist
if not os.path.exists(INPUT_DIR):
    os.makedirs(INPUT_DIR)
    print(f"Created '{INPUT_DIR}'. Please put your images there and run this script again.")
else:
    bulk_process(INPUT_DIR, OUTPUT_DIR)
