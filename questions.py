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

# Variable para llevar el puntaje # B- Linea agregada
score = 0  # B- Linea agregada

# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_input = input("Respuesta: ")

        # Verificar si el input es un número y si está en el rango válido
        if user_input.isdigit() and 1 <= int(user_input) <= len(answers[question_index]):
            user_answer = int(user_input) - 1

            # Se verifica si la respuesta es correcta
            if user_answer == correct_answers_index[question_index]:
                print("¡Correcto!")
                score += 1  # B- Linea agregada
                break
            else:
                print("Incorrecto.")
                score -= 0.5  # B- Linea agregada
        else:
            print("Respuesta no válida")
            break
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])

    # Se imprime un blanco al final de la pregunta
    print()

# Mostrar el puntaje final # B- Linea agregada
print(f"Puntaje final: {score}")  # B- Linea agregada