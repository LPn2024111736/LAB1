import funcoes as f

def main():
    print("Preciso que introduza dois valores:")
    x: float = float(input("x="))
    y: float = float(input("y="))

    val:float
    val=f.somar(x,y)
    print("Valor da soma:",val)
    val=f.subtrair(x,y)
    print("Valor da subtração:",val)
    val=f.multiplicar(x,y)
    print("Valor da multiplicação:",val)
    try:
        val = f.dividir(x, y)
        print("Valor da divisão:",val)
    except ZeroDivisionError as e:
        print("Error: ",e)
    val=f.raizquadrada(x)
    print("Valor da raíz quadrade de X:",val)


if __name__ == '__main__':
    main()
