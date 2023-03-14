import os
import sys

print("CONCATENADOR DE ARCHIVOS - BLACKZERO")
print("------------------------------------")

MES_INI=202303
MES_FIN=202313

for i in range(MES_INI, MES_FIN): #rango de fechas en donde los primeros cuatros digitos representa el año y los otros dos elmes
    fecha = str(i)

    # Ruta de la carpeta de entrada donde se encuentran los archivos de texto
    input_folder = "DIRECTORIO DE ORIGEN DONDE ESTAN LOS ARCHIVOS CONSECUTIVOS" + "\\" + fecha

    if not os.path.exists(input_folder):
        print("El directorio {} no existe. No hay más directorios por procesar.".format(input_folder))
        sys.exit()

    # Ruta de la carpeta de salida donde se guardará el archivo concatenado
    output_folder = "DIRECTORIO DE DESTINO"

    print("A continuacion concatenaran los archivos de la carpeta: ")
    print("------------------------------------")
    print(input_folder)
    print("A la carpeta ")
    print(output_folder)
    print("------------------------------------")

    # Lista para almacenar el contenido de los archivos de texto
    contenido_archivos = []
    
    PREFIX ="PREFIJO_DE_LOS_ARCHIVOS_A_PROCESAR"

    # Recorremos todos los archivos de la carpeta de entrada
    for archivo in os.listdir(input_folder):
        # Comprobamos que el nombre del archivo comience con 'LISTADO_MOVIMIENTOS_COMBINADO_'
        if archivo.startswith(PREFIX) and archivo.endswith('.txt'):
            print('Procesando archivo:', archivo)
            # Abrimos el archivo y leemos su contenido
            with open(os.path.join(input_folder, archivo), 'r') as f:
                # Leemos todas las líneas del archivo
                lineas = f.readlines()
                # Agregamos todas las líneas menos la primera a la lista
                contenido_archivos.extend(lineas[1:])

    # Unimos el contenido de todos los archivos en un solo string
    contenido_final = ''.join(contenido_archivos)
    
    FINAL_NAME="NOMBRE_ARCHIVO_FINAL_"

    # Creamos un nuevo archivo con el contenido concatenado en la carpeta de salida
    with open(os.path.join(output_folder, FINAL_NAME + fecha + '.txt'), 'w') as f:
        f.write(contenido_final)

    print("------------------------------------")
    print('Se ha creado el archivo: ' + FINAL_NAME + fecha + '.txt')
    print('con el contenido concatenado de la carpeta ' + input_folder)
