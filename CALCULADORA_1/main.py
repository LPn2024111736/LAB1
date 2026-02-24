import soma as som
import diferenca as sub
import multiplicacao as mul
import divisao as div
import raizquadrada as sqrt

def main():
    print("Qual é o cálculo que quer efetuar? x + - / *")
    res: str = input()
    print("Preciso que introduza dois valores:")
    x: float = float(input("x="))
    if res == "*":
        try:
            m: float = sqrt.raizquadrada(x)
            print("O resultado da raíz é:",m)
        except ValueError as e:
            print("Error:", e)
        exit(0)
    y: float = float(input("y="))

    if res == "x":
        z: float = mul.multiplicar(x, y)
        print("O resultado da multiplicação é:", z)
    elif res == "/":
        try:
            z = div.dividir(x, y)
            print("O resultado da divisão é:", z)
        except ZeroDivisionError as e:
            print("Error:", e)
    elif res == "+":
        m: float = som.somar(x, y)
        print("O resultado da soma é:", m)
    else:
        n: float = sub.subtrair(x, y)
        print("O resultado da subtração é:", n)


if __name__ == '__main__':
    main()
