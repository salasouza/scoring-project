import pandas as pd 
from abc import ABC, abstractmethod

class CarregadorDados(ABC):
    """ 
    Classe construida para carregamento dos dados.
    """
    @abstractmethod
    def carregador_dados(self):
        pass
    
class CarregadorCSV(CarregadorDados):
    
    def __init__(self, caminho_dados):
        self.caminho_dados = caminho_dados
    
    
    def carregador_dados(self):
        """ 
        O objetivo dessa função é carregar os dados em formato csv.
        """
        dados = pd.read_csv(self.caminho_dados, sep=',')
        if dados is None:
            print(f"Falha ao carregar os dados {self.caminho_dados}")
        
        return dados 
        
