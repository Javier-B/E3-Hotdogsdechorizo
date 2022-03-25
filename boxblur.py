#Importación de librerias
import numpy
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

#Crear padding
def pad_with(vector,pad_width,iaxis,kwargs):
    pad_value=kwargs.get('padder',10)
    vector[:pad_width[0]]=pad_value
    vector[-pad_width[1]:]=pad_value
    
#Se recibe como parametro el nombre de la imagen
def boxblur(archivo):
    #Cargar imagen
    Is=Image.open(archivo)
    #Convertir a escala de grises
    I=Is.convert('L')
    #Convertir en 0-1 para poder operar la imagen
    I=numpy.asarray(I)
    I=I/255.0

    #Convolución
    k=numpy.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
    J=ndimage.convolve(I,k,mode='constant',cval=0.0)

    #Crear grafica
    plt.figure(figsize=(15,15))
    
    #Imagen original
    plt.subplot(2,2,1)
    plt.imshow(Is)
    plt.xlabel('Imagen Original')

    #Imagen convolucionada
    plt.subplot(2,2,2)
    plt.imshow(J)
    plt.xlabel('Box Blur')

    plt.grid(False)
    plt.show()


