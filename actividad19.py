import os
import msvcrt
import csv

#FUNCION PARA CREAR TITULOS
def titulo(texto : str):
    print(f"\033[33m{texto.upper()}\033[0m")
def error(texto : str):
    print(f"\033[31m{texto.upper()}\033[0m")
def exito(texto : str):
    print(f"\033[32m{texto.upper()}\033[0m")

#Tuplas - Clases
clases = [
    ("PESAS","LUN-MIE 08:30 a.m",10),
    ("ZUMBA","MAR-JUE 3:30-5:40 p.m",20),
    ("NUTRICION","VIERNES 6:00-7:30 a.m",2),
    ("CROSSFIT","SAB 11:30-12:55 p.m",10)
]
#diccionario para usuarios
usuarios = {}
#lista -reservas
reservas = []
#CONTADOR
numero_usuario = 100

#comenzamos el sistema
while True:
    print("PRESS ANY KEY")
    msvcrt.getch()
    os.system("cls")

    print("""\033[32m
    SISTEMA GESTION FITLIFE
    ════════════════════════════════\033[0m
    1) REGISTRAR USUARIO
    2) RESERVAR CLASE
    3) CONSULTAR CLASES DISPONIBLES
    4) CONSULTAR CLASES DE USUARIO
    5) CONSULTAR USUARIOS
    0) SALIR.      
    \033[32m════════════════════════════════\033[0m""")
    opcion = (input("SELECCIONE : "))
    if opcion == "0":
        titulo("ADIOS")
        break
    elif opcion == "1":
        titulo("REGISTRAR USUARIOS")
        nombre = input("INGRESE NOMBRE DE USUARIO : ").upper()
        #VALIDAR QUE EL NOMBRE DE USUARIO NO SE REPITA
        if nombre not in usuarios.values():
            usuarios[numero_usuario] = nombre
            numero_usuario += 100
            exito("USUARIO REGISTRADO")
        else:
            error("USUARIO REPETIDO")
    elif opcion == "2":
        titulo("RESERVAR CLASE")
        codigo = int(input("INGRESE SU CODIGO DE USUARIO : "))
        if codigo in usuarios:
            curso = input("INGRESE CURSO A INSCRIBIR : ").upper()
            centinela = False
            centinelacupos = False
            for c in clases:
                if c[0].upper() == curso:
                    centinela = True
                    if c[2]>0:
                        centinelacupos = True
                        reservas.append([codigo, usuarios[codigo],c[0],c[1]])
                        exito("RESERVA REALIZADA")
                        actualizacioncupo = (c[0],c[1],c[2]-1)
                        clases.remove(c)
                        clases.append(actualizacioncupo)
                        break
            if  centinela == False:
                error("USUARIO NO EXISTE")
        else:
            error("CODIGO NO EXISTE")      

    elif opcion == "3":
        titulo("CONSULTAR CLASES DISPONIBLES")
        for c in clases:
            print(f"{c[0]}| HORARIO: {c[1]} CUPOS: {c[2]}")
    elif opcion == "4":
        titulo("CONSULTAR CLASES DE USUARIO")
    elif opcion == "5":
        titulo("CONSULTAR USUARIOS")
        if len(usuarios)>0:
            for u in usuarios:
                print(f" {u} : {usuarios[u]}")
        else:
            error("NO HAY USUARIOS REGISTRADOS")
    else:
        error("OPCION NO VALIDA")


    