from typing import Union
from math import sqrt

class Raiz:
    """
    Classe Raiz, utilizada para a realização da operação destinada a esta classe.
    :param self.x: valor a que a raíz vai ser aplicada
    :param self.res: resultado da raíz quadrada
    """
    def __init__(self, x:float,):
        self.x = x
        self.res = 0

    def executar(self)->Union[float,str]:
        """
        Executa a operação referente à classe, ou seja, faz a raíz quadrada de um valor.
        :param x: valor a que a raíz vai ser aplicada
        :return: retorna o resultado da raíz quadrada
        :raises ValueError: erro encontrado quando o número é negativo
        """
        try:
            self.res = sqrt(self.x)
        except ValueError:
            return "error:negative number"
        return self.res



