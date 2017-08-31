

#Python usa librerias como matplotlib con objetos predeterminados com$
import matplotlib.pyplot as plt
#Construimos el objeto plt introduciendo valores que se grafican cont$
plt.plot([2,2,3,5,5,6,8,8,8,9,9,11,12,12,12,12,12,13.13,13,15,16,17])
#Con esta isntruccion colocamos un titulo al eje Y de la grafica. 
plt.ylabel('Numero de hermanos y primos')
#Con esta instruccion colocamos un titulo al eje X de la grafica.
plt.xlabel('Edad')
#Con esta isntruccion guardamos la imagen con el formato que queramos.
plt.savefig('temp.png')
#Con esta instruccion mostramos la figura. 
plt.show()


