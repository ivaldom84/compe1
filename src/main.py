from ahorcado import Ahorcado



class Menu:
    def __init__(self):
        self.juegos = {
            '1': Ahorcado(),
        }

    def mostrar_menu(self):
        print("=== Menú de Juegos ===")
        print("1. Ahorcado")
        print("2. Adivina el Número")
        print("3. Trivia")
        print("0. Salir")

    def ejecutar(self):
        opcion = None
        while opcion != '0':
            self.mostrar_menu()
            opcion = input("Elige una opción: ")

            if opcion in self.juegos:
                self.juegos[opcion].jugar()
            elif opcion == '0':
                print("Gracias por jugar. ¡Hasta la próxima!")
            else:
                print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu = Menu()
    menu.ejecutar()