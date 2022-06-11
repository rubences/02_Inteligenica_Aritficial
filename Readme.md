El primer script en Python
Le proponemos realizar un proyecto que consiste en la escritura de un script Python que permite a un robot aspirador calcular la superficie de una habitación y estimar el tiempo de limpieza.
Imaginemos que la habitación que hay que limpiar contiene un mueble debajo del cual no puede meterse el robot y que tiene las siguientes características:
 
Plano de la habitación
 
Vista 3D de la habitación
Una de las formas posibles de calcular la superficie que debe limpiar el robot consiste en fragmentar la superficie total en zonas utilizables:
ZONA	LARGO (cm)	ANCHO (cm)
Zona 1	500	150
Zona 2	480	101
Zona 3	309	480
Zona 4	90	220
Una vez fragmentada, es fácil calcular la superficie total que hay que limpiar añadiendo las superficies de cada zona. Estas superficies se calculan multiplicando el largo por el ancho en cada una de ellas.
 
Zonas utilizables por el robot aspirador
Ahora que hemos definido la forma de proceder, vamos a programar el script.
