import os
import msvcrt
import csv
usuarios={}
clases={"BACHATA":("BACHATA","19:00",30),
        "SALSA":("SALSA","19:30",30),
        "TANGO":("TANGO","20:00",30)}
print("<<PRESS ANY KEY>>")
msvcrt.getch()
os.system("cls")
while True:
    print("\033[35m═══════════════════════════════════")
    print("SISTEMA DE GESTION GIMNASIO FITLIFE")
    print("═══════════════════════════════════\033[0m")
    print("1) REGISTRAR UN NUEVO USUARIO")
    print("2) RESERVAR UNA CLASE Y GENERAR REPORTE CSV")
    print("3) CONSULTAR CLASES DISPONIBLES")
    print("4) CONSULTAR RESERVAS DE UN USUARIO")
    print("0) SALIR")
    print("\033[35m═══════════════════════════════════\033[0m")
    opcion=input("SELECCIONE: ")
    if opcion=="0":
        break
    elif opcion=="1":
        os.system("cls")
        print("\033[34mREGISTRAR NUEVO USUARIO\033[0m")
        rut=int(input("INGRESE SU RUT SIN PUNTOS Y SIN GUIÓN: "))
        while rut<9999999:
            print("\033[31mRUT NO VALIDO. INTENTE NUEVAMENTE.\033[0m")
            rut=int(input("INGRESE SU RUT SIN PUNTOS Y SIN GUIÓN: "))
        nombre=input("INGRESE SU NOMBRE: ").upper()
        while len(nombre)<3:
            print("\033[31mEL NOMBRE DEBE TENER AL MENOS 3 LETRAS. INTENTE NUEVAMENTE.\033[0m")
            nombre=input("INGRESE SU NOMBRE: ").upper()
        reservas=[]
        usuarios[rut]=nombre,reservas
        print("\033[32mUSUARIO REGISTRADO CON ÉXITO.\033[0m")
    elif opcion=="2":
        os.system("cls")
        print("\033[34mRESERVAR UNA CLASE Y GENERAR REPORTE CSV\033[0m")
        rut=int(input("INGRESE SU RUT: "))
        if rut in usuarios:
            while True:
                print(f"\033[35mBIENVENID@")
                print("ESTAS SON LAS CLASES QUE TENEMOS DISPONIBLES")
                print("════════════════════════════════════════════\033[0m")
                print("1) BACHATA\t19:00")
                print("2) SALSA\t19:30")
                print("3) TANGO\t20:00")
                print("0) VOLER AL MENÚ PRINCIPAL")
                print("\033[35m════════════════════════════════════════════\033[0m")
                opcion2=input("SELECCIONE: ")
                if opcion2=="0":
                    break
                elif opcion2=="1":
                    if clases["BACHATA"][2]>0:
                        nueva_reserva=[rut,"BACHATA",clases["BACHATA"][1]]
                        reservas.append(nueva_reserva)
                        usuarios[rut]=nombre,reservas
                        clases["BACHATA"]=(clases["BACHATA"][0],clases["BACHATA"][1],clases["BACHATA"][2]-1)
                        print("\033[32mRESERVA REALIZADA CON EXITO.\033[0m")
                        with open('ACTIVIDAD 19/cantidad_reservas.csv','w',newline='',encoding='utf-8') as r:
                            escritura=csv.writer(r,delimiter=',')
                            escritura.writerows(reservas)
                    else:
                        print("\033[31mNO QUEDAN CUPOS DISPONIBLES PARA BACHATA\033[0m")
                elif opcion2=="2":
                    if clases["SALSA"][2]>0:
                        nueva_reserva=[rut,"SALSA",clases["SALSA"][1]]
                        reservas.append(nueva_reserva)
                        usuarios[rut]=nombre,reservas
                        clases["SALSA"]=(clases["SALSA"][0],clases["SALSA"][1],clases["SALSA"][2]-1)
                        print("\033[32mRESERVA REALIZADA CON EXITO.\033[0m")
                        with open('ACTIVIDAD 19/cantidad_reservas.csv','w',newline='',encoding='utf-8') as r:
                            escritura=csv.writer(r,delimiter=',')
                            escritura.writerows(reservas)
                    else:
                        print("\033[31mNO QUEDAN CUPOS DISPONIBLES PARA SALSA\033[0m")
                elif opcion2=="3":
                    if clases["TANGO"][2]>0:
                        nueva_reserva=[rut,"TANGO",clases["TANGO"][1]]
                        reservas.append(nueva_reserva)
                        usuarios[rut]=nombre,reservas
                        clases["TANGO"]=(clases["TANGO"][0],clases["TANGO"][1],clases["TANGO"][2]-1)
                        print("\033[32mRESERVA REALIZADA CON EXITO.\033[0m")
                        with open('ACTIVIDAD 19/cantidad_reservas.csv','w',newline='',encoding='utf-8') as r:
                            escritura=csv.writer(r,delimiter=',')
                            escritura.writerows(reservas)
                    else:
                        print("\033[31mNO QUEDAN CUPOS DISPONIBLES PARA TANGO\033[0m")
                else:
                    print("\033[31mOPCION NO VALIDA\033[0m")
        else:
            print("\033[31mEL RUT NO SE ENCUENTRA REGISTRADO\033[0m")
    elif opcion=="3":
        print("\033[34mCONSULTAR CLASES DISPONIBLES\033[0m")
        print(reservas)
    elif opcion=="4":
        print("\033[34mCONSULTAR RESERVAS DE UN USUARIO\033[0m")
        print(usuarios)
    else:
        print("\033[31mOPCION NO VALIDA\033[0m")