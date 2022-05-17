#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 08:39:30 2022

@author: joaquingalindo
"""


libros=[]
autores=[]
numero_serie=[]
arriendos=[]
generos=[]
fecha_arriendo=[]
fecha_regreso=[]
nombre_arrendatario=[]
existencia= False
while True:
    print(" (0) Salir \n (1) Ver inventario de la biblioteca \n (2) Manejo de arriendos \n (3) Libros por categoría \n (4) Modificar inventarios ")
    menu=input("Ingrese el número de la acción que desea realizar: ")
    if menu == "0":
        break
    elif menu == "1":
        if existencia == False:
            print()
            print("---------------------------------------------------------------------------------------------------------")
            print("Todavía no hay libros agregados al inventario, primero debes agregarlos en la opción modificar inventario")
            print("---------------------------------------------------------------------------------------------------------")
            print()
        else:
            print()
            print("-----------------------------------------------------------------------------------------------------------")
            for i in range(len(libros)):                
                print(f"El libro {libros[i]} , con autor {autores[i]}, número de serie {numero_serie[i]} y genero {generos[i]} está {arriendos[i]}")
            print("-----------------------------------------------------------------------------------------------------------")
            print()
    elif menu == "2":
        ari=input(" (1) Quieres arrendar \n (2) Quieres devolver el libro \n (3) Ver el estado del arriendo: ")
        if ari == "1":
            ask=input("Nombre del libro que quieres arrendar: ")
            po=input("Ingrese el número de serie: ")
            if ask in libros:
                inde=numero_serie.index(po) 
                if libros[inde] == ask and numero_serie[inde] == po:
                    if arriendos[inde] != "Arrendado":
                        fech_arr=input("Fecha de arriendo (Recordar que debe poner dd/mm/aaaa): ")
                        if len(fech_arr) == 10 or len(fech_arr) == 9 or len(fech_arr) == 8:
                            nombre_persona=input("A nombre de quien está el arriendo: ")
                            fech_dev=fech_arr.split("/")
                            fecha_arriendo[inde]=fech_arr
                            suma=int(fech_dev[0])+7
                            suma1=fech_dev[1]
                            ano=fech_dev[2]
                            if suma > 31:
                                suma-=31
                                suma1=int(fech_dev[1])+1
                                if suma1 > 12:
                                    suma-=12
                                    ano=int(fech_dev[2])+1
                            fecha_regreso[inde]=f"{suma}/{suma1}/{ano}"
                            nombre_arrendatario[inde]=nombre_persona
                            arriendos[inde]="Arrendado"
                            print()
                            print("-----------------------------------------------------------------------------------------------------------")
                            print(f"Tu libro ha sido arrendado con exito, debe devolverlo el {fecha_regreso[inde]} ")
                            print("-----------------------------------------------------------------------------------------------------------")
                            print()
                        else:
                            print()
                            print("-----------------------------------------------------------------------------------------------------------")
                            print(f"La fecha no es como se precisó en la instrucción")
                            print("-----------------------------------------------------------------------------------------------------------")
                            print()
                    else:
                        print()
                        print("-----------------------------------------------------------------------------------------------------------")
                        print(f"El libro ya está arrendado")
                        print("-----------------------------------------------------------------------------------------------------------")
                        print()
                else:
                    print()
                    print("-----------------------------------------------------------------------------------------------------------")
                    print(f"El libro y su número de serie no coinciden")
                    print("-----------------------------------------------------------------------------------------------------------")
                    print()
            else:
                print()
                print("-----------------------------------------------------------------------------------------------------------")
                print("El libro no esta en el inventario")
                print("-----------------------------------------------------------------------------------------------------------")
                print()
        elif ari == "2":
            ask=input("Nombre del libro que quieres devolver: ")
            po=input("Ingrese el número de serie: ")
            if ask in libros:
                inde=numero_serie.index(po) 
                if libros[inde] == ask and numero_serie[inde] == po:
                    if arriendos[inde] == "Arrendado":
                        arriendos[inde]="Disponible"
                        print()
                        print("-----------------------------------------------------------------------------------------------------------")
                        print("Tu libro ha sido regresado con exito")
                        print("-----------------------------------------------------------------------------------------------------------")
                        print()
                    else:
                        print()
                        print("-----------------------------------------------------------------------------------------------------------")
                        print("El libro está disponible")
                        print("-----------------------------------------------------------------------------------------------------------")
                        print()
                else:
                    print()
                    print("-----------------------------------------------------------------------------------------------------------")
                    print("El libro y su número de serie no coinciden")
                    print("-----------------------------------------------------------------------------------------------------------")
                    print()
                    
            else:
                print()
                print("-----------------------------------------------------------------------------------------------------------")
                print("El libro no esta en el inventario")
                print("-----------------------------------------------------------------------------------------------------------")
                print()
        elif ari == "3":
            ask=input("Nombre del libro que quieres ver el estado: ")
            po=input("Ingrese el número de serie: ")
            if ask in libros:
                inde=numero_serie.index(po)
                if libros[inde] == ask and numero_serie[inde] == po:
                    if arriendos[inde] == "Arrendado":
                        print()
                        print("-----------------------------------------------------------------------------------------------------------")
                        print(f"El libro {ask} se arrendó el {fecha_arriendo[inde]}, se debe devolver el {fecha_regreso[inde]} y lo arrendó {nombre_arrendatario[inde]}")
                        print("-----------------------------------------------------------------------------------------------------------")
                        print()
                    elif arriendos[inde] == "Disponible":
                        print()
                        print("-----------------------------------------------------------------------------------------------------------")
                        print(f"El libro está Disponible")
                        print("-----------------------------------------------------------------------------------------------------------")
                        print()
                else:
                    print()
                    print("-----------------------------------------------------------------------------------------------------------")
                    print("El libro y su número de serie no coinciden")
                    print("-----------------------------------------------------------------------------------------------------------")
                    print()
            else:
                print()
                print("-----------------------------------------------------------------------------------------------------------")
                print("El libro no esta en el inventario")
                print("-----------------------------------------------------------------------------------------------------------")
                print()            
        else:
            print()
            print("-----------------------------------------------------------------------------------------------------------")
            print("No seleccionaste ninguna de las opciones válidas")
            print("-----------------------------------------------------------------------------------------------------------")
            print()
    elif menu == "3":
        category=input("¿Quieres buscar el libro por genero o por autor? (debes poner genero o autor respectivamente): ")
        if category == "genero":
            like=input("¿Qué genero estás buscando?: ")
            like_min=like.lower()
            if like_min in generos:
                momentaneo=[]
                contador=0
                for i in generos:
                    if i == like_min:
                        momentaneo.append(f"{libros[contador]}, autor {autores[contador]} y número de serie {numero_serie[contador]}")
                    else:
                        pass
                    contador+=1
                
                print()
                print(f"Los libros disponible del Genero {like} son:")
                print("-----------------------------------------------------------------------------------------------------------")
                for i in momentaneo:
                    print(i)  
                print("-----------------------------------------------------------------------------------------------------------")
                print()
            else:
                print()
                print("-----------------------------------------------------------------------------------------------------------")
                print(f"No hay libros del genero {like} en el inventario")
                print("-----------------------------------------------------------------------------------------------------------")
                print()
        elif category == "autor":
            like1=input("¿Qué Autor estás buscando?: ")
            like1_min=like1.lower()
            if like1_min in autores:
                momentaneo1=[]
                contador1=0
                for i in autores:
                    if i == like1_min:
                        momentaneo1.append(f"{libros[contador1]}, autor {autores[contador1]} y número de serie {numero_serie[contador1]}")
                    else:
                        pass
                    contador1+=1
                
                print()
                print(f"Los libros disponible del Autor {like1} son:")
                print("-----------------------------------------------------------------------------------------------------------")
                for i in momentaneo1:
                    print(i)  
                print("-----------------------------------------------------------------------------------------------------------")
                print()
            else:
                print()
                print("-----------------------------------------------------------------------------------------------------------")
                print(f"No hay libros del autor {like1} en el inventario")
                print("-----------------------------------------------------------------------------------------------------------")
                print()
        else:
            print()
            print("-----------------------------------------------------------------------------------------------------------")
            print("No seleccionaste ninguna de las opciones válidas")
            print("-----------------------------------------------------------------------------------------------------------")
            print()
    elif menu == "4":
        disp=input("Desea eliminar o agregar un libro (poner eliminar o agregar respectivamente): ")
        if disp == "agregar":
            print()
            nombre=input("Nombre del libro: ")    
            existencia = True
            autor=input("Autor: ")
            num=input("Número de serie: ")
            if num not in numero_serie:
                genero=input("Genero: ")
                genero_min=genero.lower()
                autor_min=autor.lower()
                print()
                libros.append(nombre)
                autores.append(autor_min)
                numero_serie.append(num)
                arriendos.append("Disponible")
                generos.append(genero_min)
                fecha_arriendo.append("")
                fecha_regreso.append("")
                nombre_arrendatario.append("")
                print("-----------------------------------------------------------------------------------------------------------")
                print("El titulo ha sido agregado con exito")
                print("-----------------------------------------------------------------------------------------------------------")
                print()
            else:
                print("-----------------------------------------------------------------------------------------------------------")
                print("El numero de serie ya existe en el inventario ingresa uno que no esté")
                print("-----------------------------------------------------------------------------------------------------------")
                print()
        
        elif disp == "eliminar":
            if len(libros) == 0: 
                print("-----------------------------------------------------------------------------------------------------------")
                print("No hay libros para eliminar")
                print("-----------------------------------------------------------------------------------------------------------")
                print()
                existencia=False
            else:
                elim=input("Ingresa el nombre del título que deseas eliminar: ")
                if elim in libros:                                        
                    ind=libros.index(elim)
                    libros.pop(ind)
                    autores.pop(ind)
                    numero_serie.pop(ind)
                    arriendos.pop(ind)
                    generos.pop(ind)
                    fecha_arriendo.pop(ind)
                    fecha_regreso.pop(ind)
                    nombre_arrendatario.pop(ind)
                    print()
                    print("-----------------------------------------------------------------------------------------------------------")
                    print("Tu libro ha sido eliminado con exito")
                    print("-----------------------------------------------------------------------------------------------------------")
                    print()
                else:
                    print()
                    print("-----------------------------------------------------------------------------------------------------------")
                    print("El libro no está en el inventario")
                    print("-----------------------------------------------------------------------------------------------------------")
                    print()
            if len(libros) == 0: 
                existencia=False
            
        else:
            print()
            print("-----------------------------------------------------------------------------------------------------------")
            print("No seleccionaste ninguna de las opciones válidas")
            print("-----------------------------------------------------------------------------------------------------------")
            print()
            
            
                 
            
            
            