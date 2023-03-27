import os
import shutil
from datetime import date
from datetime import timedelta


print("COPIADOR DE ARCHIVOS - BLACKZERO")
print("--------------------------------")
print("CARGA DE ARCHIVO CSV")
print("--------------------------------")
print("Busca el ultimo archivo disponible")
print("--------------------------------")


def validarArchivo (ruta,nombre_archivo):
    print('Buscando el archivo: ' +  nombre_archivo)
    if os.path.exists(os.path.join(ruta, nombre_archivo+".txt")):
        print('Archivo encontrado')
        return 1
    else: 
        print('Archivo no encontrado')
        return 0
def copiarArchivo (origen,destino,archivo):
    print("A continuacion copiaremos el archivo " + nombre_archivo + " de la carpeta: ")
    print(origen)
    print("A la carpeta ")
    print(destino)

    # Recorremos la carpeta de origen
    for archivo in os.listdir(origen):
        
        if archivo.startswith(nombre_archivo):
            # Creamos la ruta completa del archivo de origen
            ruta_origen = os.path.join(origen, archivo)
            # Creamos la ruta completa del archivo de destino
            ruta_destino = os.path.join(destino, archivo)
            # Copiamos el archivo de origen al destino
            shutil.copyfile(ruta_origen, ruta_destino)
            # Mostramos el nombre del archivo que se está copiando
            print(f"Copiando {archivo}")

    file_oldname = os.path.join(destino, nombre_archivo+".txt")
    file_newname_newfile = os.path.join(destino, "NOMBRE DE ARCHIVO FINAL.txt")

    newFileName=shutil.move(file_oldname, file_newname_newfile)

    print ("Archivo renombrado a :",newFileName)



# Ruta de la carpeta de origen
origen = r" RUTA ARCHIVO ORIGEN" 

    # Ruta de la carpeta de destino
destino = r"RUTA FINAL"


dias = 1
hoy = date.today()
filedate = str(hoy - timedelta(days=dias))
anio = filedate[:4]
mes = filedate[5:7]
dia = filedate[8:10]
fecha = anio + mes
ruta = origen + fecha
nombre_archivo = "MAESTRO_CUENTAS_"+ anio+mes+dia


repuesta = validarArchivo(ruta,nombre_archivo)
if repuesta == 1:
    copiarArchivo(origen+fecha,destino,nombre_archivo)   

else:
    for i in range (2,30):
        dias = i
        hoy = date.today()
        filedate = str(hoy - timedelta(days=dias))
        anio = filedate[:4]
        mes = filedate[5:7]
        dia = filedate[8:10]
        fecha = anio + mes
        ruta = origen + fecha
        nombre_archivo = "PATRON DEL NOMBRE DE ARCHIVO"+ anio+mes+dia
        repuesta = validarArchivo(ruta,nombre_archivo)
        if repuesta==1:
            copiarArchivo(origen+fecha,destino,nombre_archivo) 
            break
        else:
            print('Archivo no encontrado.')