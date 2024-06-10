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


