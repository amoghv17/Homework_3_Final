import cv2

# Read the image.
img = cv2.imread('download.jpg')
bilateral = cv2.bilateralFilter(img, 15, 125, 175)
# Save the output.
cv2.imwrite('bilateral.jpg', bilateral)