class Somar:
    """
    Classe Somar, utilizada para a realização da operação destinada a esta classe.
        :param self.x: primeiro valor a ser adicionado
        :param self.y: segundo valor a ser adicionado
        :return: resultado da adição
    """
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.res = 0


    def executar(self)->float:
        """
        Executa a operação referente à classe, ou seja, adiciona dois valores.
        :param x: primeiro valor a ser adicionado
        :param y: segundo valor a ser adicionado
        :return: retorna o resultado da adição
        """
        self.res = self.x + self.y
        return self.res