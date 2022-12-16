

def some_func(a, b):
    return a * b


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