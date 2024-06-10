def zoom_mri(img, first, end): # permet de retourner l'image zommé entre 2 points ⎡ ⎦
    cropped_img = img[first[0]:end[0], first[1]:end[1]] # [ | , -- ]
    return cropped_img