import csv
import os

# Define el nombre de tu archivo de entrada y salida
input_file = "C:\\Users\\roberto.bravo\\Documents\\BI\\Tarjeta\\CierreFacturacionHist\\LISTADO_MOVIMIENTOS_COMBINADO_FINAL.txt"
output_file = 'C:\\Users\\roberto.bravo\\Documents\\BI\\Tarjeta\\FacturacionTarjetas.csv'

try:
    # Verificar si el archivo de salida ya existe
    if not os.path.exists(output_file):
        with open(output_file, 'w', newline='') as file_out:
            pass

    # Leer el archivo de entrada y escribir en el archivo de salida
    with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
        lines = file_in.readlines()
        lines = [line.strip().split('\t') for line in lines]
        writer = csv.writer(file_out)
        num_lines = len(lines)
        for i, line in enumerate(lines):
            writer.writerow(line)
            if (i + 1) % 1000 == 0:
                print(f"{i+1}/{num_lines} líneas procesadas.")
        
        # Indicar cuántas líneas se han procesado
        print(f"{num_lines} líneas procesadas.")

except FileNotFoundError:
    print(f"Error: el archivo de entrada '{input_file}' no existe.")
    
except Exception as e:
    print(f"Error: {str(e)}")
    
# Mensaje de finalización
print("El procesamiento ha finalizado.")