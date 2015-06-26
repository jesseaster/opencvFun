import pytesseract
import Image
import cv2
from PIL import Image

#im = Image.open("mhcorbin.jpg")
#im2 = im.rotate(-90)
#im2.save("rotated.jpg")

img = cv2.imread("mhcorbin.jpg")
y = 1450
y_plus_h = 1600
x = 700
x_plus_h = 1250
#Note: its img[y: y + h, x: x + w]
crop_img = img[y:y_plus_h, x:x_plus_h]
gray_img = cv2.cvtColor( crop_img, cv2.COLOR_RGB2GRAY )
cv2.imshow("gray", gray_img)


ret, binary_img = cv2.threshold(gray_img,80,255,cv2.THRESH_BINARY)
print(ret)

cv2.imshow("binary", binary_img)
cv2.imwrite("binary_img.jpg", binary_img)
print(pytesseract.image_to_string(Image.open("binary_img.jpg")))
cv2.waitKey(0)
