import multiplicacao as mul
import raizquadrada as sqrt
import soma as som
import diferenca as sub
import divisao as div
def main():
    print("Preciso que introduza dois valores:")
    x: float = float(input("x="))
    y: float = float(input("y="))

    val:float
    val=som.somar(x,y)
    print("Valor da soma:",val)
    val=sub.subtrair(x,y)
    print("Valor da subtração:",val)
    val=mul.multiplicar(x,y)
    print("Valor da multiplicação:",val)
    try:
        val = div.dividir(x, y)
        print("Valor da divisão:",val)
    except ZeroDivisionError as e:
        print("Error: ",e)
    val=sqrt.raizquadrada(x)
    print("Valor da raíz quadrade de X:",val)


if __name__ == '__main__':
    main()
