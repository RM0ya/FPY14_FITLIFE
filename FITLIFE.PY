import os
import csv
import msvcrt
datos = []

while True:
    print("""
════════════════════════════════════════    
MENÚ DE GIMNASIO FITLIFE
════════════════════════════════════════
1) REGISTRAR USUARIO
2) RESERVAR CLASE Y GUARDARLO EN UN CSV
3) CONSULTAR CLASE DISPONIBLES
4) CONSULTAR RESERVAS DE UN USUARIO
5) SALIR DEL PROGRAMA
════════════════════════════════════════""")
    opcion  = int(input("SELECCIONE : "))

    if opcion == 5:
        break
    elif opcion == 1:
        print("REGISTRAR UN USUARIO")
        rut = int(input("INGRESE SU RUT SIN PUNTOS NI GUION : "))
        while rut < len(str (rut)):
            print("RUT VALIDO : ")
            nombre = input("INGRESE SU NOMBRE Y APELLIDO").upper()

        else:
            print("RUT INCORRECTO, POR FAVOR INGRESE SU RUT CORRECTAMENTE")
            rut = input("INGRESE SU RUT SIN PUNTOS NI GUION")
    elif opcion == 2:
        print("REGISTRAR UN USUARIO")
    elif opcion == 3:
        print("REGISTRAR UN USUARIO")
    elif opcion == 4:
        print("REGISTRAR UN USUARIO")