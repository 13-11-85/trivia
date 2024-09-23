import random

# Función para dar la bienvenida y validar la edad del jugador
def bienvenida():
    nombre = input("Ingrese su nombre: ")
    
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.")
    
    if edad >= 18:
        print(f"♥️ ¡Bienvenido al juego de Capitales, {nombre}! ♥️")
        print("Ya puedes comenzar a jugar.")
        print("Este juego consiste en responder correctamente las preguntas por medio de opción múltiple.")
        print("¡Comencemos! Mucha suerte ♣️.")
        print("\n")
        return nombre, True
    else:
        print("¡Lo sentimos! Debes ser mayor de edad para jugar. Gracias por intentarlo ♥️")
        return nombre, False

# Función que realiza la lógica de preguntas y respuestas
def jugar_trivia(nombre):
    preguntas = [
        ("1 - ¿Cuál es la capital de Perú?", ["a- La Paz", "b- Lima", "c- Quito"], "b"),
        ("2 - ¿Cuál es la capital de Francia?", ["a- Berlín", "b- Roma", "c- París"], "c"),
        ("3 - ¿Cuál es la capital de Japón?", ["a- Seúl", "b- Tokio", "c- Beijing"], "b"),
        ("4 - ¿Cuál es la capital de Australia?", ["a- Sídney", "b- Canberra", "c- Melbourne"], "b"),
        ("5 - ¿Cuál es la capital de Canadá?", ["a- Toronto", "b- Ottawa", "c- Vancouver"], "b")
    ]
    
    random.shuffle(preguntas)
    puntaje = 0
    maximo_errores = 3
    
    for pregunta, opciones, respuesta_correcta in preguntas:
        errores_consecutivos = 0  # Reiniciar contador de errores por cada pregunta

        while errores_consecutivos < maximo_errores:
            print(pregunta)
            for opcion in opciones:
                print(opcion)

            respuesta = input("Ingrese la opción (a/b/c): ")
            if respuesta == respuesta_correcta:
                print("La respuesta es correcta.\n")
                puntaje += 1
                break 
            else:
                errores_consecutivos += 1  
                print("La respuesta es incorrecta.\n")
                
        if errores_consecutivos == maximo_errores:
            print("Has cometido tres errores consecutivos. Terminó el juego.")
            break
                
    print(f"🎉 ¡Has terminado el juego, {nombre}! 🎉")
    print(f"Obtuviste {puntaje} respuestas correctas de {len(preguntas)}.\n")
    print("¡Gracias por jugar! Esperamos verte pronto en otra trivia. ¡Hasta luego! 😊")

# Función principal que ejecuta el juego
def juego_trivia():
    nombre, es_mayor = bienvenida()
    if es_mayor:
        jugar_trivia(nombre)

# Inicia el juego
juego_trivia()
 