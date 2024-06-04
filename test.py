import cv2 as cv
import matplotlib.pyplot as plt
import zoom, show, contrast



image = cv.imread('image/Y1.jpg', cv.IMREAD_GRAYSCALE)

zoomed = zoom.zoom_mri(image, (50, 400), (300, 500))
plt.figure(figsize=(20,5))
plt.subplot(1,9,1), show.show(image, 'frjk')
plt.subplot(1,9,2), show.show(image, 'frjk')
plt.subplot(1,9,3), show.show(image, 'frjk')
plt.subplot(1,9,4), show.show(image, 'frjk')
plt.subplot(1,9,5), show.show(image, 'Accent'), plt.title('Accent')
plt.subplot(1,9,6), show.show(image, 'gray'), plt.title('gray')
plt.subplot(1,9,7), show.show(image, 'magma'), plt.title('magma')
plt.subplot(1,9,8), show.show(image, 'terrain'), plt.title('terrain')
plt.subplot(1,9,9), show.show(image, 'jet'), plt.title('jet')
plt.show()

[log, gamma, neg] = contrast.contrast(image)
plt.subplot(1,4,1),show.show(log, 'magma')
plt.subplot(1,4,2),show.show(gamma, 'magma')
plt.subplot(1,4,3),show.show(neg, 'magma')
plt.subplot(1,4,4),show.show(image, 'magma')
plt.show()