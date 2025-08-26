import random

def input_con_validacion(prompt):
    try:
        s = input(prompt)
        return s
    except Exception as e:
        print("Error al ingresar el dato:", e)
        return input_con_validacion(prompt)

def juego_adivina_numero():
    print("Bienvenido al juego: ¡El computador intentará adivinar tu número!")
    print("Piensa en un número entre 1 y 100, y yo trataré de adivinarlo.")
    print("Responde con: 'mayor', 'menor' o 'igual'.\n")

    bajo = 1
    alto = 100
    intentos = 0

    while True:
        intentos += 1
        if bajo > alto:
            print("Parece que hubo un error en tus respuestas 😅.")
            break

        adivinanza = random.randint(bajo, alto)
        respuesta = input_con_validacion(f"¿Es {adivinanza} tu número? (mayor/menor/igual): ").strip().lower()

        if respuesta == "igual":
            print(f"¡Genial! Adiviné tu número en {intentos} intentos 🎉.")
            break
        elif respuesta == "mayor":
            bajo = adivinanza + 1
        elif respuesta == "menor":
            alto = adivinanza - 1
        else:
            print("Respuesta no válida. Escribe 'mayor', 'menor' o 'igual'.")

if __name__ == "__main__":
    juego_adivina_numero()
