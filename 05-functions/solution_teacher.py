def devolver_distintos(a, b, c):
    suma = a + b + c
    lista = [a, b, c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]


def get_unique_letters_teacher(word):
    my_set = set()

    for letter in word:
        my_set.add(letter)

    my_list = list(my_set)
    my_list.sort()

    return my_list


def has_consecutive_zeros_teacher(*args):
    counter = 0

    for num in args:
        if counter + 1 == len(args):
            return False
        elif args[counter] == 0 and args[counter + 1] == 0:
            return True
        else:
            counter += 1

    return False

def count_cousins(limit):
    cousins = [2]
    iteration = 3

    if limit < 2:
        return 0

    while iteration <= limit:
        for n in range(3, iteration, 2):
            if iteration % n == 0:
                iteration += 2
                break
            else:
                cousins.append(iteration)
                iteration += 2

    print(cousins)
    return len(cousins)
