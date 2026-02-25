

class Multiplicar:
    """
    Classe Multiplicar, utilizada para a realização da operação destinada a esta classe.
    :param self.x: primeiro valor a ser multiplicado
    :param self.y: segundo valor a ser multiplicado
    :param self.res: resultado da multiplicação
    """
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.res = 0


    def executar(self)->float:
        """
        Executa a operação referente à classe, ou seja, multiplica dois valores.
        :param x: primeiro valor a ser multiplicado
        :param y: segundo valor a ser multiplicado
        :return: retorna o resultado da multiplicação
        """
        self.res = self.x * self.y
        return self.res
