import os
import shutil

print("COPIADOR DE ARCHIVOS - BLACKZERO")
print("--------------------------------")

fecha='FECHA DEL ARCHIVO' # Mes en curso 

# Ruta de la carpeta de origen
origen = "CARPETA DONDE SE ENCUENTRA EL ARCHIVO" + "\\" + fecha

# Ruta de la carpeta de destino
destino = "RUTA DE LA CARPETA DESTINO" + "\\" + fecha

print("A continuacion copiaremos los archivos de la carpeta: ")
print(origen)
print("A la carpeta ")
print(destino)

# Creamos la carpeta de destino si no existe
if not os.path.exists(destino):
    os.makedirs(destino)

PREFIX="PREFIJO_DEL_ARCHIVO"

# Recorremos la carpeta de origen
for archivo in os.listdir(origen):
    # Si el archivo empieza con cualquier patron ingresado en la variable prefijo
    if archivo.startswith(PREFIX):
        # Creamos la ruta completa del archivo de origen
        ruta_origen = os.path.join(origen, archivo)
        # Creamos la ruta completa del archivo de destino
        ruta_destino = os.path.join(destino, archivo)
        # Copiamos el archivo de origen al destino
        shutil.copyfile(ruta_origen, ruta_destino)
        # Mostramos el nombre del archivo que se está copiando
        print(f"Copiando {archivo}")

print("TODOS LOS ARCHIVOS SE HA COPIADO SATISFACTORIAMENTE")