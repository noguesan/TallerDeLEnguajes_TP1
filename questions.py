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
answers = [   #answers es una lista de tuplas
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

# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index]) # imprime la pregunta aleatoria
    for i, answer in enumerate(answers[question_index]):  #Enumerate: itera sobre una secuencia para obtener tanto el índice como el valor de cada elemento en la iteración.
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2): # range(2): genera una secuencia de números del 0 al 1
        user_input = input("Respuesta: ")

        # Verificar si el input es un número #LINEA AGREGADA
        if user_input.isdigit(): #LINEA AGREGADA
            user_answer = int(user_input) - 1  # Restamos 1 para ajustar a los índices de las respuestas

            # Verificar si la respuesta está dentro del rango válido #LINEA AGREGADA
            if user_answer >= 0 and user_answer < len(answers[question_index]): #LINEA AGREGADA
                # Se verifica si la respuesta es correcta
                if user_answer == correct_answers_index[question_index]:
                    print("¡Correcto!")
                    break
                else:
                    print("Incorrecto.")
            else:
                print("Respuesta no válida") #LINEA AGREGADA
                break
        else:
            print("Respuesta no válida") #LINEA AGREGADA
            break

        """
        El else del for:
          El else en Python, cuando se usa con un bucle for, se ejecuta siempre que el bucle no sea interrumpido por un break.
          En este caso, el break se usa cuando el usuario responde correctamente, lo que hace que el bucle termine inmediatamente.
          Si el usuario no responde correctamente en los dos intentos, el bucle terminará sin que se ejecute un break, y se ejecutará
          el bloque else. Esto es lo que se usa para mostrar la respuesta correcta después de que los dos intentos hayan fallado.
        """
    else:  # Este else pertenece al ciclo for
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])

    # Se imprime un blanco al final de la pregunta
    print()