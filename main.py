

def some_func(a, b):
    return a * b


def binary_search(iteration: list, item):
    """
    Метод позовляет найти индекс item в списке iteration с помощью бинарного (Логорифмического) поиска
    """
    low = 0
    high = len(iteration) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = iteration[mid]
        if guess == item:
            return f"index = {mid}"
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


def log(numeral, base=2):
    """
    Метод преднозначен для подсчета логорифма от: numeral, с осонованием: base
    numeral: число
    base: основание (по-умолчанию = 2)
    """
    y = 0
    while numeral > 1:
        y += 1
        numeral = numeral / base

    return y

