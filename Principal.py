import os
from Terreno.terreno import terreno as t
from Draw.draw import draw as d



# -----------------------------------------------------
# configuración del sistema de percolación
# -----------------------------------------------------


# probabilidad de que haya agua en la posición
p = float(input("probabilidad de que haya agua en la posición: "))
# tamaño del terreno
tamano = int(input("Tamaño del terreno: "))


# tamaño por defecto de la pantalla
tamanoPantalla = 500

# tamaño de la pantalla segun tamaño del terreno
if tamano <= 16:
    tamanoPantalla = tamano*40
elif tamano <= 30:
    tamanoPantalla = tamano*20
else:
    tamanoPantalla = 600

# Limpiar pantalla
os.system('cls')

# -----------------------------------------------------
# Crear terreno para el sistema
# -----------------------------------------------------


suelo = [[0] * tamano for i in range(tamano)]
agua = [[0] * tamano for i in range(tamano)]

generarTerreno = t(p,suelo,agua)

# crear suelo
generarTerreno.crearSuelo()

# crear zonas de agua
generarTerreno.rociarAgua()


# mostrar el suelo
print("-----------------------------------------------------")
print("                     SUELO                           ")
print("-----------------------------------------------------")
for i in range(tamano):
        for j in range(tamano):
            print(suelo[i][j],end='\t')
        print("")

print("")
# mostrar las Zonas de agua
print("-----------------------------------------------------")
print("                      AGUA                           ")
print("-----------------------------------------------------")
for i in range(tamano):
        for j in range(tamano):
            print(agua[i][j],end='\t')
        print("")

print("")


terreno = d(tamano,tamanoPantalla,suelo,agua)

# configurar el tamaño de las imagenes
terreno.config()

# -----------------------------------------------------
# Iniciar el sistema de percolación
# -----------------------------------------------------

terreno.simulacionAgua()
