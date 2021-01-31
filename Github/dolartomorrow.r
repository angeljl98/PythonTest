install.packages("tidyverse")
install.packages("rgl") # Renderizacion a tiempo real  de gráficos 3D por medio de openGL.
install.packages("magick") # Librería necesaria para exportar los gráficos en formato GIF.
install.packages("MASS") # Librería necesaria para soportar funciones Venables y Ripley.
install.packages("RNetCDF") # Librería necesaria para lectura de arfivos *.nc.
install.packages("plot3Drgl") # Ciertas funciones para crear Graficos 3D.
install.packages("OceanView") # Interpretación de datos oceanográficos.
install.packages("Marelac") # Conjuntos de datos, constantes, factores de conversión y utilidades para las ciencias 'Marinas'.

library(tidyverse)
plot3d(x, y, z,
	xlab, ylab, zlab, type = "p", col,
	size, lwd, radius,
	add = FALSE, aspect = !add,
	xlim = NULL, ylim = NULL, zlim = NULL,
	forceClipregion = FALSE, ...)

w=unlist(Dolartdy[,1])
x=unlist(Dolartdy[,2])
y=unlist(Dolartdy[,3])
z=unlist(Dolartdy[,4])
