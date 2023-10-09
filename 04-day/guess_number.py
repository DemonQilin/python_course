from random import randint

# Inicializar variables
tries = 8
tried_numbers = []
secret_number = randint(1, 100)

# Saludo y captura del nombre del jugador
print("\n===================== THE GUESS NUMBER GAME =====================\n")
player_name = input("To start the game, enter your name: > ")

# Explicación del juego
print()
print(f"Hello {player_name.upper()}, I thought a number between 1 and 100.")
print(f"You has {tries} attempts to guess the number")

# Inicio de intentos de adivinar
for attempt in range(1, tries + 1):
    # Indicar el número de intento el que se encuentra el jugador
    attempt = attempt if attempt >= 10 else '0' + str(attempt)
    print(f"\n\nAttempt {attempt}\n")

    # Captura y validación del número apostado por el jugador
    tried_number = 0
    while True:
        typed_number = input("Type a number between 1 and 100: > ")

        # Comprobación de que sea un número válido, de lo contrario vuelve a preguntar
        try:
            tried_number = int(typed_number)
            break
        except ValueError:
            print(f'"{typed_number}" is not a valid integer. Try again.')

    # Analisis de número elegido por el jugador
    if tried_number in tried_numbers:
        print("Oh oh, you lost an attempt with a number you had already entered :(")
    elif tried_number not in range(1, 101):
        print("The number you have chosen is not in the range between 1 and 100.")
    elif tried_number < secret_number:
        print("You have chosen a number less than the secret number.")
    elif tried_number > secret_number:
        print("You have chosen a number greater than the secret number.")
    else:
        print(f"\nCongratulations {player_name.upper()}!!!")
        print(
            f"You have won! The secret number was {secret_number} and it took you {attempt} tries.\n")
        break

    tried_numbers.append(tried_number)
else:
    # Mensaje de despedida al acabarse los intentos
    print(
        f"\nYou have failed to guess the secret number {secret_number} and have wasted all your attempts. Next time be the good one ;)")
print("\n===================== END GUESS NUMBER GAME =====================\n")
