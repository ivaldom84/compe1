import random

class Ahorcado:
    def __init__(self):
        self.palabras = ['python', 'programacion', 'ahorcado', 'juego']
        self.intentos_maximos = 6

    def elegir_palabra(self):
        return random.choice(self.palabras)

    def jugar(self):
        palabra = self.elegir_palabra()
        letras_adivinadas = []
        intentos_restantes = self.intentos_maximos

        print(f"¡Bienvenido al juego del Ahorcado! La palabra tiene {len(palabra)} letras.")

        while intentos_restantes > 0 and set(letras_adivinadas) != set(palabra):
            print(f"\nPalabra: {' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])}")
            print(f"Intentos restantes: {intentos_restantes}")

            letra = input("Adivina una letra: ").lower()
            if letra in palabra and letra not in letras_adivinadas:
                letras_adivinadas.append(letra)
            else:
                intentos_restantes -= 1

        if set(letras_adivinadas) == set(palabra):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
        else:
            print(f"Lo siento, te has quedado sin intentos. La palabra era: {palabra}")
2
