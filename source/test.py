import cv2 as cv
import matplotlib.pyplot as plt
import zoom, show, contrast
import base64
from io import BytesIO
from PIL import Image
import numpy as np



image = cv.imread('../image/Y3.jpg', cv.IMREAD_GRAYSCALE)

zoomed = zoom.zoom_mri(image, (50, 400), (300, 500))
show.show(zoomed, 'magma')


[log, gamma, neg] = contrast.contrast(image)


img = cv.imread('../client/src/image/Y3.jpg', cv.IMREAD_GRAYSCALE)
#fact_resp= model.predict(img)


filename='../client/src/image/Y3.jpg'
with open(filename, 'rb') as imgfile:
    base64_bytes = base64.b64encode(imgfile.read())
    base64_encoded = base64_bytes.decode()

print(base64_encoded)

#im = Image.open(BytesIO(img))
#im.save('image1.jpg', 'JPG')

#encoded_string = base64.b64encode('../client/src/image/Y3.jpg')
#print('\n\n', data.decode('utf-8'))
#print('\n\n', img)
#print('\n\n', encoded_string)
#print('\n\n', encoded_string.decode('utf-8'))

def zoom_mri(image, firstX, firstY, endX, endY): # permet de retourner l'image zommé entre 2 points ⎡ ⎦
    img = cv.imread('../client/src/image/'+image, cv.IMREAD_GRAYSCALE)
    cropped_img = img[firstX:endX, firstY:endY] # [ | , -- ]
    cv.imwrite('../client/src/image/zoom.jpg', cropped_img)

zoom_mri('original.jpg', 0,0,100,100)


