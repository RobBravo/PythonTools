import os
import sys

print("CONCATENADOR DE ARCHIVOS - BLACKZERO")
print("------------------------------------")

for i in range(202303, 202313): #rango de meses a procesar
    fecha = str(i)

    # Ruta de la carpeta de entrada donde se encuentran los archivos de texto
    input_folder = r"C:\Users\roberto.bravo\Documents\BI\Tarjeta\CierreFacturacionHist" + "\\" + fecha

    if not os.path.exists(input_folder):
        print("El directorio {} no existe. No hay más directorios por procesar.".format(input_folder))
        sys.exit()

    # Ruta de la carpeta de salida donde se guardará el archivo concatenado
    output_folder = r"C:\Users\roberto.bravo\Documents\BI\Tarjeta\CierreFacturacionHist"

    print("A continuacion concatenaran los archivos de la carpeta: ")
    print("------------------------------------")
    print(input_folder)
    print("A la carpeta ")
    print(output_folder)
    print("------------------------------------")

    # Lista para almacenar el contenido de los archivos de texto
    contenido_archivos = []

    # Recorremos todos los archivos de la carpeta de entrada
    for archivo in os.listdir(input_folder):
        # Comprobamos que el nombre del archivo comience con 'LISTADO_MOVIMIENTOS_COMBINADO_'
        if archivo.startswith('LISTADO_MOVIMIENTOS_') and archivo.endswith('.txt'):
            print('Procesando archivo:', archivo)
            # Abrimos el archivo y leemos su contenido
            with open(os.path.join(input_folder, archivo), 'r') as f:
                # Leemos todas las líneas del archivo
                lineas = f.readlines()
                # Agregamos todas las líneas menos la primera a la lista
                contenido_archivos.extend(lineas[1:])

    # Unimos el contenido de todos los archivos en un solo string
    contenido_final = ''.join(contenido_archivos)

    # Creamos un nuevo archivo con el contenido concatenado en la carpeta de salida
    with open(os.path.join(output_folder, 'LISTADO_MOVIMIENTOS_COMBINADO_' + fecha + '.txt'), 'w') as f:
        f.write(contenido_final)

    print("------------------------------------")
    print('Se ha creado el archivo LISTADO_MOVIMIENTOS_COMBINADO_' + fecha + '.txt')
    print('con el contenido concatenado de la carpeta ' + input_folder)
