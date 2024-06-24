print(""" 
*******MUNDO LIBRO*******
 """)

libros_agregados = []


lista_de_reportes = []


while True:
        opc = int(input(""" INGRESE UNA DE LAS SIGUIENTES OPCIONES
        1) - MANTENEDOR DE LIBROS
        2) - REPORTES
        3) - SALIR
                 """))

        if opc == 2:
                reporte = input("ingrese su reporte: ")
                lista_de_reportes.append(reporte)
                print(f"REPORTES: {lista_de_reportes}")

        if opc == 3:
                print("SALIENDO DEL PROGRAMA")
                break
        
        if opc == 1:
                print("Abriendo lista de opciones...")
                opciones = int(input(""" INGRESE UNA DE LAS SIGUIENTES OPCIONES
        1) - AGREGAR LIBRO
        2) - EDITAR LIBRO
        3) - ELIMINAR LIBRO
        4) - BUSCAR LIBRO
        5) - VOLVER
                 """))
                if opciones == 1:
                        agregando_libros = int(input("ingrese el ID del libro que desee agregar: "))
                        libros_agregados.append(agregando_libros)
                        print(f"LIBROS AGREGADOS {libros_agregados}")
                if opciones == 2:
                        id_de_libro_edit = int(input("ingrese el ID del libro que desee editar: "))
                        titulo_edit = input("ingrese el nuevo titulo del libro: ")
                        autor_edit = int(input("ingrese el nombreID del autor: "))
                        categoria_edit = int(input("ingrese la categoriaID del libro: "))
                        ano_public_edit = int(input("ingrese el AnoPublicacion del libro: "))
                if opciones == 3:
                        libro_descartado = int(input("ingrese el ID del libro que desee eliminar: "))
                        libros_agregados.pop(libro_descartado)
                        print(f"los libros fueron descartados, ahora su lista se actualizó a: {libros_agregados}")
                if opciones == 4:
                        libro_por_id = int(input("Escriba el ID de su libro y se pondrá el titulo del libro: "))
                        if libro_por_id == 1:
                                print("su libro es (CIEN AÑOS DE SOLEDAD)")
                        if libro_por_id == 2:
                                print("su libro es (LA CASA DE LOS ESPIRITUS)")
                        if libro_por_id == 3:
                                print("su libro es (RAYUELA)")
                        if libro_por_id == 4:
                                print("su libro es (LA CIUDAD Y LOS PERROS)")
                        if libro_por_id == 5:
                                print("su libro es (LA SOMBRA DEL VIENTO)")
                        if libro_por_id == 6:
                                print("su libro es (FICCIONES)")
                        if libro_por_id == 7:
                                print("su libro es (DON QUIJOTE DE LA MANCHA)")
                        if libro_por_id == 8:
                                print("su libro es (VEINTE POEMAS DE AMOR Y UNA CANCION DESESPERADA)")
                        if libro_por_id == 9:
                                print("su libro es (BODAS DE SANGRE)")
                        if libro_por_id == 10:
                                print("su libro es (EL LABERINTO DE LA SOLEDAD)")
                        if libro_por_id == 11:
                                print("su libro es (EL AMOR EN LOS TIEMPOS DEL COLERA)")
                        if libro_por_id == 12:
                                print("su libro es (EVA LUNA)")
                        if libro_por_id == 13:
                                print("su libro es (BESTIARIO)")
                        if libro_por_id == 14:
                                print("su libro es (LA FIESTA DEL CHIVO)")
                        if libro_por_id == 15:
                                print("su libro es (EL JUEGO DEL ANGEL)")
                        if libro_por_id == 16:
                                print("su libro es (EL ALEPH)")
                        if libro_por_id == 17:
                                print("su libro es (NOVELAS EJEMPLARES)")
                        if libro_por_id == 18:
                                print("su libro es (RESIDENCIA EN LA TIERRA)")
                        if libro_por_id == 19:
                                print("su libro es (LA CASA DE BERNARDA ALBA)")
                        if libro_por_id == 20:
                                print("su libro es (PIEDRA DE SOL)")
                        if libro_por_id == 21:
                                print("No existe ningun libro con ese ID")
                if opciones == 5:
                        print("volviendo...")
                        continue