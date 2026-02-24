from Operacoes import dividir, subtrair, somar, raiz, multiplicar


#import interface
def main():
    print("Preciso que introduza dois valores:")
    x:float = float(input("x="))
    y:float = float(input("y="))
    s:object = somar.Somar(x, y)
    res = s.executar()
    print("O valor da operação somar é:", res)
    s:object = dividir.Dividir(x, y)
    res = s.executar()
    if type(res)==str:
        print (res)
    else:
        print("O valor da operação divisão é:",res)
    s:object = subtrair.Subtrair(x, y)
    res = s.executar()
    print("O valor da operação subtrair é:", res)
    s:object = multiplicar.Multiplicar(x, y)
    res = s.executar()
    print("O valor da operação multiplicar é:", res)
    s:object = raiz.Raiz(x)
    res = s.executar()
    if type(res)==str:
        print (res)
    print("O valor da operação raiz (x) é:", res)
    s:object = raiz.Raiz(y)
    res = s.executar()
    if type(res)==str:
        print (res)
    print("O valor da operação raiz (y) é:", res)


if __name__ == '__main__':
    main()
