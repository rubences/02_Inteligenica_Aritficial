#-------------------------------------------------------

#----------------------------------------------
# FUNCIONES
#----------------------------------------------

def calculoDeLaSuperficieALimpiar(listaDeZonas):
    superficieALimpiar = 0
    for zona in listaDeZonas:
        largo = zona.get("largo")/100
        ancho = zona.get("ancho")/100
        calculo = largo*ancho
        print (str(largo)+" x "+str(ancho)+"= "+str(calculo))
        superficieALimpiar = superficieALimpiar +calculo
    return (superficieALimpiar)


def tiempoLimpiezaEnMinutos(superficieALimpiar, tiempoParaUnMetroCuadrado):
    return round(superficieALimpiar*tiempoParaUnMetroCuadrado)

#----------------------------------------------
# APLICACION
#----------------------------------------------

#Empleo de una tupla para la configuración de la aplicación
#Nombre del robot, tiempo en minutos para limpiar un metro cuadrado
parametros = ("robot_aspirador",2)

# Empleo de diccionarios para crear las zonas
zona1={"largo":500,"ancho":150}
zona2={"largo":309,"ancho":480}
zona3={"largo":101,"ancho":480}
zona4={"largo":90,"ancho":220}

# Empleo de una lista que permite guardar las zonas
zonas = []
zonas.append(zona1)
zonas.append(zona2)
zonas.append(zona3)
zonas.append(zona4)

#Llamada de la función que permite calcular la superficie a limpiar
superficieALimpiar = calculoDeLaSuperficieALimpiar(zonas)
print("La superficie total a limpiar es de: "+str(superficieALimpiar)+ " m2")

#Llamada de la función que permite determinar el tiempo de limpieza
tiempoEstimado = tiempoLimpiezaEnMinutos(superficieALimpiar,parametros[1])
print("El tiempo estimado es: "+str(tiempoEstimado)+" minutos")

#Añade una condición que se activa en función del tiempo de limpieza
if tiempoEstimado > 55:
    print(parametros[0]+" dice: ¡Me parece que esto va a tardar un poco!")