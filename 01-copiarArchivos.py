import os
import shutil
from datetime import date
from datetime import timedelta

print("COPIADOR DE ARCHIVOS - BLACKZERO")
print("--------------------------------")

# Mes en curso 

dias = 1
hoy = date.today()
filedate = str(hoy - timedelta(days=dias))
anio = filedate[:4]
mes = filedate[5:7]
dia = filedate[8:10]
fecha = anio + mes 

# Ruta de la carpeta de origen
origen = r" " + "\\" + fecha

# Ruta de la carpeta de destino
destino = r" " + "\\" + fecha

print("A continuacion copiaremos los archivos de la carpeta: ")
print(origen)
print("A la carpeta ")
print(destino)

# Creamos la carpeta de destino si no existe
if not os.path.exists(destino):
    os.makedirs(destino)

# Recorremos la carpeta de origen
for archivo in os.listdir(origen):
    # Si el archivo empieza con "LISTADO_MOVIMIENTOS_"
    if archivo.startswith("LISTADO_MOVIMIENTOS_"):
        # Creamos la ruta completa del archivo de origen
        ruta_origen = os.path.join(origen, archivo)
        # Creamos la ruta completa del archivo de destino
        ruta_destino = os.path.join(destino, archivo)
        # Copiamos el archivo de origen al destino
        shutil.copyfile(ruta_origen, ruta_destino)
        # Mostramos el nombre del archivo que se está copiando
        print(f"Copiando {archivo}")

print("TODOS LOS ARCHIVOS SE HA COPIADO SATISFACTORIAMENTE")
