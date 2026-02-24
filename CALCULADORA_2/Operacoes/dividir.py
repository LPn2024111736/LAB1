from typing import Union

class Dividir:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.res = 0


    def executar(self)->Union[float,str]:
        """
        Executa a operação referente à classe, ou seja, divide dois valores.
        :param x: dividendo
        :param y: divisor
        :return: retorna o resultado da divisão
        :raises ZeroDivisionError: erro encontrado com divisão por 0
        """
        try:
            self.res = self.x / self.y
        except ZeroDivisionError:
            return "error:dividing by zero"
        return self.res
