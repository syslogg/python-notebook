from biblioteca.fisica.basico import Basico
from biblioteca.fisica.ultrapassagem import Ultrapassagem
from biblioteca.fisica.mu import MU
from biblioteca.fisica.muv import MUV


class Cinematica(object):
    """
    Classe que organiza todos os tópicos de cinemática.
    """

    BASICO = 1
    ULTRAPASSAGEM = 2
    MU = 3
    MUV = 4

    def __init__(self, operacao):
        """
        Constructor of kinematics topics
        """

        if operacao == self.BASICO:
            self.cinematica = Basico()
        elif operacao == self.ULTRAPASSAGEM:
            self.cinematica = Ultrapassagem()
        elif operacao == self.MU:
            self.cinematica = MU()
        elif operacao == self.MUV:
            self.cinematica = MUV()
        else:
            raise NameError("Operação Invalida!")

    def calcular(self, operacao, **kwargs):
        """
        Calcular operações de cinemática.
        """

        return self.cinematica.calcular(operacao, kwargs)
