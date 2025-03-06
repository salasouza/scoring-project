import pandas as pd 
from abc import ABC, abstractmethod

class LimpezaDados(ABC):
    """
    Classe construindo para alocar as funções de limpezado do conjunto de dados
    """
    @abstractmethod 
    def remover_variaveis_int_object(self, dados):
        pass 
    
    @abstractmethod
    def remover_variaveis_nulos(self, dados):
        pass
    
    @abstractmethod
    def remover_variaveis_zeros(self, dados):
        pass
    
    @abstractmethod
    def imputar_metodo_zeros_nulos(self, dados, metodo):
        pass 
    
class AplicacoesLimpeza(LimpezaDados):
    # def __init__(self, valor_corte, metodo):
    #     self.valor_corte = valor_corte
    #     self.metodo = metodo 
        
    def remover_variaveis_int_object(self, dados):
        """
        Essa função tem por objetivo remover as variavies int e object
        """
        # dados_numericos = dados
        col_object = []
        col_int = []
        if dados is None:
            print('Falha na Leitura dos dados')
        
        for col in dados.columns:
            if dados[col].dtypes =='object':
                col_object.append(col)
            elif dados[col].dtypes =='int64':
                col_int.append(col)
                
        dados_ = dados.drop(columns=col_object, axis=1) 
        dados_numericos = dados_.drop(columns=col_int, axis=1) 
        
        if dados_numericos is None:
            print('Falha ao contruir os dados numericos')
        
        return dados_numericos
    
    def remover_variaveis_nulos(self, dados: pd.DataFrame, valor_corte: float) -> pd.DataFrame:
        
        """
        O objetivo dessa função é remover as colunas/variáveis que apresentam um valor limite de nulos permitidos 
        
        Entrada:
        dados: Dataframe completo
        valor_corte = Valor float de limite de corte
        
        Saída:        
        data_cleaned = DataFrame com as variáveis removidas

        """

        dados_limpos = dados.dropna(thresh=int((1-valor_corte)*len(dados)), axis=1)
        
        if dados_limpos is None:
            print('Falha para construir os dados_limpos')
        
        return dados_limpos
    
    def remover_variaveis_zeros(self, dados: pd.DataFrame, valor_corte: float)->pd.DataFrame:
        """ 
        O objetivo dessa função é remover as variavéis que contenham percentual de zeros acima do valor de corte
        
        Entrada:
        dados: DataFrame completo 
        
        Saída:
        dados : Dataframe contendo com as variáveis removidas
        """
        limite = valor_corte * int(len(dados))
        
        dados_limpos = dados.loc[:, (dados.eq(0).sum(axis=0) < limite)]
        
        return dados_limpos
    
    def imputar_metodo_zeros_nulos(self, dados : pd.DataFrame, metodo: str='mean') -> pd.DataFrame:
    
        """ 
        O objetivo dessa função é inputar nos dados faltantes o método (Média, Moda ou Mediana) apropriado.
        
        Entrada:
        dados : Dataframe contendo os dados completos
        metodo : 
            Esse método poder ser média, mediana ou moda sendo o método 'mean' o padrão da função.
            
        Saída:
        dataframe: Dados com as os valores inputados 
        """
        if metodo =='mean':
            return dados.fillna(dados.mean())
        elif metodo == 'moda':
            return dados.fillna(dados.mode.iloc(0))
        elif metodo =='median':
            return dados.fillna(dados.median())
        
        else:
            raise ValueError("Falha ao reconhecer o método! Use 'mean', 'mode' ou 'median'")
        
    def remover_variaveis_um_unico_valor(self, data: pd.DataFrame)-> pd.DataFrame:
        """ 
        Remove as colunas que apresentam apenas um único valore repetido
        """ 
        data = data.loc[:, data.nunique() > 1]
        return data