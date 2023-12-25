import cv2
import easyocr
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import base64
from skimage.morphology import (square, rectangle, diamond, disk, octagon)


reader = easyocr.Reader(['en'], gpu=False)

image_o = cv2.imread('original.png')
image_e = cv2.imread('photoshoper/pics/light/4x1.jpg')
######
result = cv2.subtract(image_o, image_e)
result2 = cv2.subtract(image_e, image_o)
#######
# cv2.imwrite('result.jpg', result)
# cv2.imwrite('result2.jpg', result2)
####
add=cv2.add(result,result2)
# cv2.imwrite('add.jpg',add)

####
gray_image = cv2.cvtColor(add, cv2.COLOR_BGR2GRAY)
(thresh, binary) = cv2.threshold(gray_image, 10, 255, cv2.THRESH_BINARY)

#######
# cv2.imshow("Gray Image",gray_image)
#
# cv2.imshow("binarry",binary)
########

# kernel = np.ones((2, 2), np.uint8)
kernel = disk(2)
img = cv2.erode(binary, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=2)

# kernel = np.ones((4, 4), np.uint8)


kernel = disk(3)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=3)
img = cv2.dilate(img, kernel, iterations=3)

# img = cv2.medianBlur(img, 21)
# cv2.imshow("Black and White Image",img)
##############
results = reader.readtext(img, detail=0)
print(results)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

