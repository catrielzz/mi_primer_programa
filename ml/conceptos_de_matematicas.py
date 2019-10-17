import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

from sklearn.datasets import make_circles

#Creamos nuestros datos artificiales, donde buscaremos clasificar
#dos anillos concentricos de datos.
X, Y = make_circles(n_samples=500, factor=0.5, noise=0.05)

#Resolucion del mapa de prediccion
res = 100

# Coordenadas del mapa de predicion
_x0 = np.linspace(-1.5, 1.5, res)
_x1 = np.linspace(-1.5, 1.5, res)

#Input con cada combo de coordenadas del mapa de prediccion
_pX = np.array(np.meshgrid(_x0, _x1)).T.reshape(-1, 2)

#Objeto vacio a 0.5 del mapa de prediccion
_pY = np.zeros((res, res)) + 0.5

#Visualizacion del mapa de prediccion.
plt.figure(figsize=(8, 8))
plt.pcolormesh(_x0, _x1, _pY, cmap="coolwarm", vmin=0, vmax=1)

#Visualizacion de la nube de datos.
plt.scatter(X[Y == 0.0], X[Y == 0.1], c="skyblue")
plt.scatter(X[Y == 1.0], X[Y == 1.1], c="salmon")

plt.tick_params(labelbottom=False, labelleft=False)
