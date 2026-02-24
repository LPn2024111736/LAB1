import Operacoes.multiplicar as multiplicar
import Operacoes.raiz as raiz
import Operacoes.somar as somar
import Operacoes.subtrair as subtrair
import Operacoes.dividir as dividir


class Interface:
    def __init__(self):
        self.x = 0
        self.y = 0


    def executar(self)->None:
        print("Qual é o cálculo que quer efetuar? x + - / *")
        res: str = input()
        print("Preciso que introduza dois valores:")
        self.x = float(input("x="))
        self.y = float(input("y="))
        if res == "+":
            s: object = somar.Somar(self.x, self.y)
            res = s.executar()
            print("O valor da operação somar é:", res)
        elif res == "/":
            s: object = dividir.Dividir(self.x, self.y)
            res = s.executar()
            if type(res) == str:
                print(res)
            else:
                print("O valor da operação divisão é:", res)
        elif res == "-":
            s: object = subtrair.Subtrair(self.x, self.y)
            res = s.executar()
            print("O valor da operação subtrair é:", res)
        elif res == "x":
            s: object = multiplicar.Multiplicar(self.x, self.y)
            res = s.executar()
            print("O valor da operação multiplicar é:", res)
        elif res == "*":
            s: object = raiz.Raiz(self.x)
            res = s.executar()
            if type(res) == str:
                print(res)
            print("O valor da operação raiz (x) é:", res)
            s: object = raiz.Raiz(self.y)
            res = s.executar()
            if type(res) == str:
                print(res)
            print("O valor da operação raiz (y) é:", res)

