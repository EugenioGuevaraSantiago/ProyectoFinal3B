print("Hecho por Eugenio Guevara Santiago y Romero Pérez Azul")

class Cancion:
    def _init_(self, nombre="", banda="", genero="", duracion=0, album="", año=0, produccion="", instrumental="", fama="", letra=""):
        self.nombre = nombre
        self.banda = banda
        self.genero = genero
        self.duracion = duracion
        self.album = album
        self.año = año
        self.produccion = produccion
        self.instrumental = instrumental
        self.fama = fama
        self.letra = letra

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar (Alta)")
    print("2. Consultar (Mostrar)")
    print("3. Modificar (Editar)")
    print("4. Eliminar (Borrar)")
    print("5. Salir")

def agregar_cancion(canciones):
    try:
        nombre = input("Ingrese el nombre de la canción: ")
        banda = input("Ingrese el nombre de la banda o artista: ")
        genero = input("Ingrese el género de la música: ")
        duracion = float(input("Ingrese la duración de la canción (en minutos): "))
        album = input("Ingrese el nombre del álbum: ")
        año = int(input("Ingrese el año de lanzamiento: "))
        produccion = input("Ingrese la producción de la canción: ")
        instrumental = input("¿Es una canción instrumental? (Sí/No): ")
        fama = input("¿Qué tan famosa es la canción? (Popular/Desconocida): ")
        letra = input("Ingrese la letra de la canción: ")

        cancion = Cancion(nombre, banda, genero, duracion, album, año, produccion, instrumental, fama, letra)
        canciones.append(cancion)
        print("Canción agregada exitosamente.")
    except ValueError:
        print("Error: Ingrese valores válidos para los campos de duración o año.")

def consultar_canciones(canciones):
    if canciones:
        print("\nLista de canciones:")
        for idx, cancion in enumerate(canciones, 1):
            print(f"\nCanción {idx}:")
            print(f"Nombre: {cancion.nombre}")
            print(f"Banda/Artista: {cancion.banda}")
            print(f"Género: {cancion.genero}")
            print(f"Duración: {cancion.duracion} minutos")
            print(f"Álbum: {cancion.album}")
            print(f"Año: {cancion.año}")
            print(f"Producción: {cancion.produccion}")
            print(f"Instrumental: {cancion.instrumental}")
            print(f"Fama: {cancion.fama}")
            print(f"Letra: {cancion.letra}")
    else:
        print("No hay canciones para mostrar.")

def modificar_cancion(canciones):
    if canciones:
        try:
            idx = int(input(f"Ingrese el número de la canción a modificar (1 a {len(canciones)}): ")) - 1
            if 0 <= idx < len(canciones):
                cancion = canciones[idx]
                print(f"\nModificando la canción: {cancion.nombre}")
                cancion.nombre = input(f"Nuevo nombre (actual: {cancion.nombre}): ") or cancion.nombre
                cancion.banda = input(f"Nuevo nombre de la banda/artista (actual: {cancion.banda}): ") or cancion.banda
                cancion.genero = input(f"Nuevo género (actual: {cancion.genero}): ") or cancion.genero
                duracion = input(f"Nueva duración (actual: {cancion.duracion}): ")
                if duracion:
                    cancion.duracion = float(duracion)
                album = input(f"Nuevo álbum (actual: {cancion.album}): ")
                if album:
                    cancion.album = album
                año = input(f"Nuevo año (actual: {cancion.año}): ")
                if año:
                    cancion.año = int(año)
                cancion.produccion = input(f"Nueva producción (actual: {cancion.produccion}): ") or cancion.produccion
                cancion.instrumental = input(f"Nueva información instrumental (actual: {cancion.instrumental}): ") or cancion.instrumental
                cancion.fama = input(f"Nuevo nivel de fama (actual: {cancion.fama}): ") or cancion.fama
                cancion.letra = input(f"Nueva letra (actual: {cancion.letra}): ") or cancion.letra
                print("Canción modificada exitosamente.")
            else:
                print("Número de canción no válido.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    else:
        print("No hay canciones para modificar.")

def eliminar_cancion(canciones):
    if canciones:
        try:
            idx = int(input(f"Ingrese el número de la canción a eliminar (1 a {len(canciones)}): ")) - 1
            if 0 <= idx < len(canciones):
                canciones.pop(idx)
                print("Canción eliminada exitosamente.")
            else:
                print("Número de canción no válido.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    else:
        print("No hay canciones para eliminar.")

def main():
    contraseña = "musica123"
    contraseñaIngresada = input("Ingrese la contraseña para acceder al menú: ")
    
    if contraseñaIngresada != contraseña:
        print("Contraseña incorrecta. Fin del programa.")
        return
    
    canciones = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            agregar_cancion(canciones)
        elif opcion == "2":
            consultar_canciones(canciones)
        elif opcion == "3":
            modificar_cancion(canciones)
        elif opcion == "4":
            eliminar_cancion(canciones)
        elif opcion == "5":
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if _name_ == "_main_":
    main()