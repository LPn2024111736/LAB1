def dividir(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y
