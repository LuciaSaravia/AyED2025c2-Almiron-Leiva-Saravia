from modules.temperaturas_imp import Temperatura_DB
from datetime import datetime  

def implementacion():
    db = Temperatura_DB()
    #abrir el archivo 
    with open ("data/muestras.txt","r") as archi:
        for linea in archi:
            linea=linea.strip()
            if linea=="":
                continue
            try:
                #separar los valores por ;
                partes=linea.split(";")
                fecha_str=  partes[0]
                temp_str=partes[1]

                #convertir fecha y temp:
                fecha= datetime.strptime(fecha_str,"%d/%m/%Y")
                temperatura= float(temp_str)

                #guardar datos
                db.guardar_temperatura(temperatura,fecha)
            except Exception as e:
                print(f"Error en la linea: {linea}. Error: {e}")
    print("Carga de datos completa")

    #uso las funciones:
    print("Cantidad de muestras cargadas:", db.cantidad_muestras())

    buscar_f=datetime.strptime("15/04/2025","%d/%m/%Y")
    print(f"Temperatura en la fecha {buscar_f.date()}: ", db.devolver_temperatura(buscar_f))

    buscar_f1=datetime.strptime("20/04/2025","%d/%m/%Y") #busque con un dia que sabia que estaba no probe con uno que no }este
    buscar_f2=datetime.strptime("25/04/2025","%d/%m/%Y")
    print(f"Temperaturas entre {buscar_f1.date()} y {buscar_f2.date()}: ", db.devolver_temperaturas(buscar_f1, buscar_f2))

    print("Temperatura maxima entre esas fechas: ", db.max_temp_rango(buscar_f1, buscar_f2))
    print("Temperatura minima entre esas fechas: ", db.min_temp_rango(buscar_f1, buscar_f2))
    print("Temperaturas extremas (min, max) entre esas fechas: ", db.temp_extremos_rangos(buscar_f1, buscar_f2))

   # NO ANDA CORREGIR
   # borrar_f=datetime.strptime("10/04/2025","%d/%m/%Y") #probe con una fecha que estaba
    #print(f"Borrando la temperatura del dia {borrar_f.date()}") 
    #db.borrar_temperatura(borrar_f)
    #print("Cantidad de muestras luego de borrar:", db.cantidad_muestras())

if __name__ == "__main__":
    implementacion()
 