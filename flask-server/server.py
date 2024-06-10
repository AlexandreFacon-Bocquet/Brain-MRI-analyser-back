from os import wait

from flask import Flask, render_template, jsonify, request, make_response
from flask_cors import CORS
from flask import Flask, jsonify, send_file
from flask_cors import CORS, cross_origin
import cv2 as cv
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import json
import contrast
from skimage import io

app = Flask(__name__)
cors = CORS(app, support_credentials=True)


def save():
    dir = '../client/src/image/mri2.jpg'
    image = cv.imread(dir, cv.IMREAD_GRAYSCALE)
    plt.imshow(image)
    plt.savefig(dir)
    return dir


# permet d'afficher l'image originale
@app.route('/show/<string:file>')  # , methods=['GET'])
@cross_origin(supports_credentials=True)
def show(file: str):
    filename = '../client/src/image/' + file  # Y4.jpg'
    file = cv.imread(filename, cv.IMREAD_GRAYSCALE)
    cv.imwrite('../client/src/image/original.jpg', file)
    cv.imwrite('../client/src/image/changed.jpg', file)
    with open(filename, 'rb') as imgfile:
        base64_bytes = base64.b64encode(imgfile.read())
        base64_encoded = base64_bytes.decode()

    return {
        "message": "Image retrieved successfully!",
        "base64": base64_encoded
    }


# permet de set une image filtrée et retourner la bonne direction
@app.route('/setFilter/<string:color>', methods=['POST'])
@cross_origin(supports_credentials=True)
def setFilter(color: str):
    directory = '../client/src/image/changed.jpg'
    image = cv.imread(directory, cv.IMREAD_GRAYSCALE)

    if color == 'jet':
        cv.imwrite(directory, cv.applyColorMap(image, cv.COLORMAP_JET))
    elif color == 'magma':
        cv.imwrite(directory, cv.applyColorMap(image, cv.COLORMAP_MAGMA))
    elif color == 'viridis':
        cv.imwrite(directory, cv.applyColorMap(image, cv.COLORMAP_VIRIDIS))
    else:
        cv.imwrite(directory, image)

    return {"route": "src/image/changed.jpg"}


@app.route('/contrast/<float:alpha>/<float:gamma>/<string:choice>', methods=['POST'])
@cross_origin(supports_credentials=True, origins="*")
def contrastImage(gamma: float, alpha: float, choice: str):
    try:
        img = cv.imread('../client/src/image/original.jpg', cv.IMREAD_GRAYSCALE)
        [log_img, gamma_img, neg_img] = contrast.contrastGeneral(img, alpha, gamma)

        if choice == 'log':
            cv.imwrite('../client/src/image/changed.jpg', log_img)
        if choice == 'neg':
            cv.imwrite('../client/src/image/changed.jpg', neg_img)
        if choice == 'gamma':
            cv.imwrite('../client/src/image/changed.jpg', gamma_img)

    except cv.error:
        contrastImage(gamma, alpha, choice)

    return "contrast changed successfully"

@app.route('/zoom/<string:image>/<int:firstX>/<int:firstY>/<int:endX>/<int:endY>', methods=['POST'])
@cross_origin(supports_credentials=True, origins="*")
def zoom_mri(image:str, firstX:int, firstY:int, endX:int, endY:int): # permet de retourner l'image zommé entre 2 points ⎡ ⎦
    img = cv.imread('../client/src/image/'+image)#, cv.IMREAD_GRAYSCALE)
    cropped_img = img[firstX:endX, firstY:endY] # [ | , -- ]
    cv.imwrite('../client/src/image/zoom.jpg', cropped_img)
    return "zoom changed successfully"


if __name__ == "__main__":
    app.run(debug=True)

