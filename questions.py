import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [   # answers es una lista de tuplas
    ("size()", "len()", "length()", "count()"),   # 1
    ("3.14", "'42'", "10", "True"),               # 2
    ("input()", "scan()", "read()", "ask()"),     # 3
    (
        "// Esto es un comentario",               # 4
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),                     # 5
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Variable para llevar el puntaje
score = 0

# Seleccionar 3 preguntas al azar junto con sus respuestas y la respuesta correcta
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)  # D- Linea agregada
"""
random.sample() selecciona elementos aleatorios de una secuencia sin reemplazo, lo que significa que ninguna pregunta se repetirá en la partida.
"""


# Iterar sobre las preguntas seleccionadas
for question, options, correct_index in questions_to_ask:  # C- Linea agregada
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_input = input("Respuesta: ")

        # Verificar si el input es un número y si está en el rango válido
        if user_input.isdigit() and 1 <= int(user_input) <= len(options):
            user_answer = int(user_input) - 1

            # Se verifica si la respuesta es correcta
            if user_answer == correct_index:
                print("¡Correcto!")
                score += 1
                break
            else:
                print("Incorrecto.")
                score -= 0.5
        else:
            print("Respuesta no válida")
            break
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(options[correct_index])  # C- Linea agregada

    print()

# Mostrar el puntaje final
print(f"Puntaje final: {score}")