import random

aleatorio = random.randint(1, 50)
print(f'Random integer = {aleatorio}')

aleatorio = round(random.uniform(1, 5), 2)
print(f'Random with uniform probability between 1 y 5: {aleatorio}')

aleatorio = random.random()
print(f'Random number between 0 y 1: {aleatorio}')

languages = ['rust', 'javascript', 'python', 'elixir', 'C']
aleatorio = random.choice(languages)
print(f'Available languages are {languages}')
print(f'Random language for you is: {aleatorio.capitalize()}')

likes_for_languages = [9, 7, 8, 5, 5]
languages = list(zip(languages, likes_for_languages))
languages.sort(key=lambda language: language[1])
print(f'Language with the scores: {languages}')
random.shuffle(languages)
print(f'Shuttle languages muajaja: {languages}')
