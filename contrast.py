import numpy as np
import cv2 as cv

def img_log(img, alpha):
    c = 255 / np.log(1 + alpha * np.max(img))
    log_image = c * (np.log(1 + alpha * img))
    return np.array(log_image, dtype=np.uint8)

def img_gamma(img, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype(np.uint8)
    return cv.LUT(img, table)

def img_neg(img_log):
    return 255 - np.array(img_log, dtype=np.uint8)
def contrast (img, alpha=0.01, gamma=0.50) :

    log_image = img_log(img, alpha)
    gamma_image = img_gamma(log_image,gamma)

    image_neg =  img_neg(log_image)

    return log_image, gamma_image, image_neg