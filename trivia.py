class Trivia:
    def _init_(self):
        self.preguntas = [
            {"pregunta": "¿Cuál es la capital de Francia?", "respuesta": "parís"},
            {"pregunta": "¿Cuántos planetas hay en el sistema solar?", "respuesta": "8"},
            {"pregunta": "¿Quién escribió 'Cien años de soledad'?", "respuesta": "gabriel garcía márquez"},
            {"pregunta": "¿Cuál es el océano más grande?", "respuesta": "pacífico"},
            {"pregunta": "¿Qué elemento químico tiene el símbolo 'O'?", "respuesta": "oxígeno"}
        ]
        self.puntaje = 0

    def hacer_pregunta(self, pregunta):
        respuesta = input(pregunta + " ").lower()
        return respuesta

    def jugar(self):
        for item in self.preguntas:
            respuesta_usuario = self.hacer_pregunta(item["pregunta"])
            if respuesta_usuario == item["respuesta"]:
                print("¡Correcto!")
                self.puntaje += 1
            else:
                print(f"Incorrecto. La respuesta correcta es: {item['respuesta']}")
        
        print(f"Tu puntaje final es: {self.puntaje}/{len(self.preguntas)}")


def main():
    juego = Trivia()
    print("¡Bienvenido al juego de Trivia!")
    juego.jugar()


if _name_ == "_main_":
    main()
