import pyodbc

print("CARGADOR DE BASES DE DATOS - BLACKZERO")
print("------------------------------------")

print("Carga de movimientos de diarios de tarjeta de credito")
print("------------------------------------")


# 1. Conexión a la base de datos
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=sql03;DATABASE=an_planeacion;Trusted_Connection=yes;')

# 2. Creación de un cursor para ejecutar consultas SQL
cursor = cnxn.cursor()

# 3. Eliminar registros de marzo 2023
query_delete = "DELETE FROM an_planeacion.BP.MOVIMIENTOS_TARJETAS_HIST WHERE YEAR(FECHA_LIQUIDACION)=2023 AND MONTH(FECHA_LIQUIDACION)=3"
cursor.execute(query_delete)
cnxn.commit()

print("Registros previos del mes en curso borrados")
print("------------------------------------")

# 4. Apertura del archivo de texto y lectura de su contenido
carpeta =r'C:\Users\roberto.bravo\Documents\BI\Tarjeta\CierreFacturacionHist' 
archivo_name = 'LISTADO_MOVIMIENTOS_COMBINADO_202303.txt'
final_file_input = carpeta + "\\" + archivo_name

with open(final_file_input, 'r') as f:
    lines  = f.readlines()

# mostrar el número de líneas que se van a procesar
print(f'Se van a procesar {len(lines)} líneas del archivo {archivo_name}.\n')


# procesar cada línea del archivo txt y agregarla a la base de datos
cursor = cnxn.cursor()
for i, line in enumerate(lines):
    fields = line.strip().split('\t')
    query = "INSERT INTO BP.MOVIMIENTOS_TARJETAS_HIST (PRODUCTO,SUBPRODUCTO,CENTRO_ALTA,CUENTA,IDENTIFICACION,NOMBRE_CLIENTE,FECHA_APERTURA_CUENTA,ESTADO_CUENTA,TARJETA_TITULAR,ESTADO_TARJETA,TARJETA_DE_LA_TRANSACCION,MONEDA_DE_LA_TRANSACCION,TIPO_FACTURA,DESCRIPCION_TIPO_FACTURA,FECHA_TRANSACCION,FECHA_LIQUIDACION,MONTO_TRANSACCION,NATURALEZA_TRANSACCION,NUMERO_AUTORIZACION,NOMBRE_COMERCIO,ANULADO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?,?, ?, ?)"
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