import pyodbc

print("CARGADOR DE BASES DE DATOS - BLACKZERO")
print("------------------------------------")

print("Descripcion de la base de datos a cargar")
print("------------------------------------")


# 1. Conexión a la base de datos
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=nombre_servidor;DATABASE=nombre_bd;Trusted_Connection=yes;')

# 2. Creación de un cursor para ejecutar consultas SQL
cursor = cnxn.cursor()

# 3. Eliminar registros de marzo 2023
query_delete = "DELETE FROM BASE_DE_DATOS WHERE COLUMNA=CRITERIO"
cursor.execute(query_delete)
cnxn.commit()

print("Descripcion de los registros borrados")
print("------------------------------------")

# 4. Apertura del archivo de texto y lectura de su contenido
carpeta ='Ruta de la carpeta del archivo origen' 
archivo_name = 'Nombre del archivo' #Puede ser txt o csv
final_file_input = carpeta + "\\" + archivo_name

with open(final_file_input, 'r') as f:
    lines  = f.readlines()

# mostrar el número de líneas que se van a procesar
print(f'Se van a procesar {len(lines)} líneas del archivo {archivo_name}.\n')


# procesar cada línea del archivo txt y agregarla a la base de datos
cursor = cnxn.cursor()
for i, line in enumerate(lines):
    fields = line.strip().split('\t')
    query = "INSERT INTO BASE_DE_DATPS (CAMPO1,CAMPO2,CAMPO3) VALUES (?, ?, ?)"
    cursor.execute(query, fields)
    if (i + 1) % 1000 == 0:
      print(f'Línea {i+1} insertada correctamente en la base de datos.')

# 6. Confirmación de los cambios en la base de datos
cnxn.commit()

# 7. Cierre del cursor y la conexión
cursor.close()
cnxn.close()

# mostrar mensaje de finalización
print('\nProceso completado correctamente.')