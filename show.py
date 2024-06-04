import matplotlib.pyplot as plt
def show(image, color_map): # permet de plot l'image avec un filtre spécifique, sinon c'est en gris
    if (color_map == 'gray' or color_map == 'Accent' or color_map == 'magma' or color_map == 'terrain' or color_map == 'jet') :
        return plt.imshow(image, cmap=color_map)
    else :
        return plt.imshow(image, cmap='gray')
