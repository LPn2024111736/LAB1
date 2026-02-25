from math import sqrt

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
    return sqrt(x)

def main():
    print("Preciso que introduza dois valores:")
    x: float = float(input("x="))
    y: float = float(input("y="))

    val:float
    val=somar(x,y)
    print("Valor da soma:",val)
    val=subtrair(x,y)
    print("Valor da subtração:",val)
    val=multiplicar(x,y)
    print("Valor da multiplicação:",val)
    try:
        val = dividir(x, y)
        print("Valor da divisão:",val)
    except ZeroDivisionError as e:
        print("Error: ",e)
    val=raizquadrada(x)
    print("Valor da raíz quadrade de X:",val)


if __name__ == '__main__':
    main()
