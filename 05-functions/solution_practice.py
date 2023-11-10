def devolver_distintos(num1, num2, num3):
    num_list = [num1, num2, num3]
    num_list.sort()

    total = sum(num_list)

    if total < 10:
        return num_list[0]
    elif total <= 15:
        return num_list[1]
    else:
        return num_list[2]


def get_unique_letters(word):
    letters = list(set(word.lower()))
    letters.sort()

    return letters


def has_consecutive_zeros(*args):
    text = "".join([str(num) for num in args])
    has_pattern = '00' in text

    return has_pattern


def count_cousins(limit):
    cousins = []

    for number in range(2, limit + 1):
        for divider in range(2, number):
            if number % divider == 0:
                break
        else:
            cousins.append(number)

    print(cousins)
    return len(cousins)

