import random

class NumeroAdivina:
    def _init_(self):
        self.rango = (1, 100)

    def jugar(self):
        numero_secreto = random.randint(*self.rango)
        intentos = 0
        adivinado = False

        print(f"¡Bienvenido al juego de Adivinar el Número! Adivina un número entre {self.rango[0]} y {self.rango[1]}.")

        while not adivinado:
            intento = int(input("Introduce un número: "))
            intentos += 1

            if intento < numero_secreto:
                print("El número es mayor.")
            elif intento > numero_secreto:
                print("El número es menor.")
            else:
                adivinado = True

        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")