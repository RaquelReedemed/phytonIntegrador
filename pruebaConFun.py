#Detalles a corregir: mejorar nombres de variables // algunas opciones faltan terminar(ej: lo de id, titulos, etc)

def opciones_menu():
    numero = input("Elija una opción: ")
    if numero == "1":
        print(submenu_1)
        ABM_peliculas()
    elif numero == "2":
        calificacion_titulos()
    elif numero == "3":
        print(submenu_3)
        reportes_estadisticas()
    elif numero == "4":
        salir_programa()
    else:
        opciones_menu()
    return "Muchas gracias por usar CINEMA+" #"Aca sale none y no se que poner o hacer pa' que eso no pase"

def ABM_peliculas():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        alta_nueva_pelicula()
    elif opcion_submenu == "2":
        print(opcion2_submenu_1)
        modificacion_pelicula_existente()
    elif opcion_submenu == "3":
        print(opcion3_submenu_1)
        baja_pelicula()
    elif opcion_submenu == "4":
        volver_menu()
    else:
        ABM_peliculas()
def calificacion_titulos():
    print(submenu_2)
def reportes_estadisticas():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        print(opcion1_submenu_3)
    elif opcion_submenu == "2":
        print(opcion2_submenu_3)
    elif opcion_submenu == "3":
        print(opcion3_submenu_3)
    elif opcion_submenu == "4":
        print(opcion4_submenu_3)
    else:
        reportes_estadisticas()
def salir_programa():
    print("Saliste del programa, Muchas gracias por utilizar CINEMA+")

def alta_nueva_pelicula():
    print(opcion1_submenu_1)
def modificacion_pelicula_existente():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        id_peli = int(input("Ingrese el id de la pelicula: "))
        print(f"La id de la peli es {id_peli}")
    elif opcion_submenu == "2":
        titulo_peli = input("Ingrese el titulo de la pelicula: ")
    elif opcion_submenu == "3":
        print(submenu_1)
        ABM_peliculas()
    else:
        modificacion_pelicula_existente()
def baja_pelicula():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        int(input("Ingrese el id de la pelicula: "))
    elif opcion_submenu == "2":
        input("Ingrese el titulo de la pelicula: ")
    elif opcion_submenu == "3":
        print(opcion3_subsubsubmenu_1)
    else:
        baja_pelicula()
def volver_menu():
    print(menu)
    opciones_menu()

#TODO
#MENU
menu = "CINEMA+ \n 1. ABM de películas \n 2. Calificación de títulos \n 3. Reportes y estadísticas \n 4. Salir"

# Menu OPCION 1 (SUBMENU OP 1)
submenu_1 = "CINEMA+ \n Alta, Baja y modificación de películas \n 1. Alta de nueva película \n 2. Modificación de película existente \n 3. Baja de película (eliminar) \n 4. Volver"
# Opciones del submenu 1 del menu (Esto es de las opciones de arriba)
opcion1_submenu_1 = "Todavia no"
opcion2_submenu_1 = "CINEMA+ \n Modificar película existente \n 1. Buscar por id \n 2. Buscar por titulo \n 3. Volver"
opcion3_submenu_1 = "CINEMA+ \n Eliminar una película existente \n 1. Buscar por id \n 2. Buscar por titulo \n 3. Volver"
opcion4_submenu_1 = "Volver"

# Opciones del submenu 2 del submenu 1 (Esto es de las opcion 2 de lo de arriba)
#opcion1_subsubmenu_1 = int(input("Ingrese el id de la pelicula: "))
#opcion2_subsubmenu_1 = input("Ingrese el titulo de la pelicula: ")
opcion3_subsubmenu_1 = "Volver"

# Opciones del submenu 3 del submenu 1 (Esto es de las opcion 3 de lo de arriba arriba)
#opcion1_subsubsubmenu_1 = int(input("Ingrese el id de la pelicula: "))
#opcion2_subsubsubmenu_1 = input("Ingrese el titulo de la pelicula: ")
opcion3_subsubsubmenu_1 = "Volver"


# Menu OPCION 2 (SUBMENU OP 2)
submenu_2 = "CALIFICACION DE TITULOS"

# Menu OPCION 3 (SUBMENU OP 3)
submenu_3 = "CINEMA+ \n Reportes y estadísticas \n 1. Listado de películas \n 2. Películas de mayor puntaje \n 3. Porcentaje de películas disponibles en la plataforma \n 4. Volver"
# Opciones del submenu 3 del menu
opcion1_submenu_3 = "Titulo, Género(s), Calificación ordenado por titulo"
opcion2_submenu_3 = "Listar titulo, género y calificación de las 15 películas de mayor puntaje."
opcion3_submenu_3 = "Imprimir histograma en porcentaje con * de películas disponible contra películas no disponibles."
opcion4_submenu_3 = "Antes de salir, debe preguntarle al usuario si desea finalizar el programa."

# Menu OPCION 4 (SUBMENU OP 4)
submenu_4 = "Saliste del programa. BYE"

print(f"{menu}")

opcion_elegida = opciones_menu()
print(opcion_elegida)