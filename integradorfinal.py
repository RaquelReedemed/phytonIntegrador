#menu
ABM_de_películas = 1
Calificación_de_títulos = 2
Reportes_y_estadísticas = 3
Salir = 4

print("CINEMA+")
#TODO 
print("Bienvenidos a CINEMA+")
print("1. ABM de películas")
print("2. Calificación de títulos")
print("3. Reportes y estadísticas")
print("4. Salir")



opcionUsuario = int(input("ingrese la opcion que desea :"))
while opcionUsuario == 1 or 2 or 3 or 4:


    if opcionUsuario == 1:
        print("CINEMA+\n Alta, Baja y modificación de películas \n 1. Alta de nueva película \n 2. Modificación de película existente \n 3. Baja de película (eliminar)\n4. Volver")
    elif opcionUsuario == 2:
        print("opcion 2")
    elif opcionUsuario == 3:
        print("CINEMA+\n Reportes y estadisticas \n 1. Listado de peliculas \n 2. Peliculas de mayor puntaje \n 3. Porcentaje de peliculas disponibles en la plataforma \n4. Volver")
    elif opcionUsuario == 4:
        print("opcion 4")
    else:
        print("opción invalida")
    break
