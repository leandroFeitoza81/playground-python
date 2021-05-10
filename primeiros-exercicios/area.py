PI = 3.14


def square(side):
    """Calcula a area de um quadrado"""
    return side * side


def rectangle(length, width):
    """Calcula a area de um retangulo"""
    return length * width


def circle(radius):
    """Calcula a area de um circulo"""
    return PI * radius * radius


if __name__ == "__main__":
    print("Area do quadrado", square(10))
    print("Area de retêngulo", rectangle(2, 2))
    print("Area do circulo", circle(3))
