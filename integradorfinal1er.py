#menu

            
continuar = True

""" opcionUsuario = int(input("ingrese la opcion que desea :")) """
while continuar:
    print("""
          Bienvenidos a CINEMA
          1. ABM de películas
          2. Calificación de títulos
          3. Reportes y estadísticas
          4. Salir
         """)

    opcionUsuario = int(input("ingrese la opcion que desea :"))

    if opcionUsuario == 1:
        while continuar:
          print("""
          CINEMA
          Alta, Baja y modificación de películas
          1. Alta de nueva película
          2. Modificación de película existente
          3. Baja de película (eliminar)
          4. Volver      
         """)
          
          subOpcionUsuario = int(input("ingrese la opcion que desea submenu :"))
        
          if subOpcionUsuario == 1:  
               print("opcion 1")
               break
          elif subOpcionUsuario == 2:
                print("""
                1. Buscar por id
                2. Buscar por titulo
                3. Volver                        
                """)
                break
          else:
              print("Opcion no valida")

    elif opcionUsuario == 2:
        print("opcion 2")
    elif opcionUsuario == 3:
        print("CINEMA+\n Reportes y estadisticas \n 1. Listado de peliculas \n 2. Peliculas de mayor puntaje \n 3. Porcentaje de peliculas disponibles en la plataforma \n4. Volver")
    elif opcionUsuario == 4:
        print("opcion 4")
    else:
        print("opción invalida")
    break





