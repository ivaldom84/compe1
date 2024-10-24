def solicitar_entrada(mensaje: str, valido: callable = None) -> str:
    while True:
        entrada = input(mensaje)
        if valido is None or valido(entrada):
            return entrada
        print("Entrada inválida. Inténtalo de nuevo.")
