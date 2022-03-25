#Importación de librerias
import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

#Crear padding
def pad_with(vector,pad_width,iaxis,kwargs):
    pad_value=kwargs.get('padder', 10)
    vector[:pad_width[0]]=pad_value
    vector[-pad_width[1]:]=pad_value

#Se recibe como parametro el nombre de la imagen
def sharpen(archivo):
    #Cargar imagen
    Is=Image.open(archivo)
    #Convertir a escala de grises
    I=Is.convert('L')
    #Convertir en 0-1 para poder operar la imagen
    I=numpy.asarray(I)
    I=I/255.0
    I=numpy.pad(I,30,pad_with,padder=1)

    #Convolución
    k=numpy.array([[0,-1,0],[-1,5,1],[0,-1,0]])
    J=ndimage.convolve(I,k,mode='constant',cval=0.0)
  
    #Crear Gráfica
    plt.figure(figsize=(15,15))
  
    #Imagen original
    plt.subplot(2,2,1)
    plt.imshow(Is)
    plt.xlabel('Imagen Original')

    #Imagen convolucionada
    plt.subplot(2,2,2)
    plt.imshow(J)
    plt.xlabel('Sharpen')

    #Plot de las imagenes
    plt.grid(False)    
    plt.show()


