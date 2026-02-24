import math
def subtrair(x: float, y: float) -> float:
    """
    Subtrai dois números
    :param x: valor subtraido
    :param y: valor a subtrair
    :return: retorna o resultado da subtraçao
    """
    return x - y


def somar(x: float, y: float) -> float:
    return x + y


def dividir(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


def multiplicar(x: float, y: float) -> float:
    return x * y

def raizquadrada( x: float) -> float:
    return math.sqrt(x)