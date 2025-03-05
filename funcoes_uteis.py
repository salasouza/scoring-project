import pandas as pd 
import numpy as np 


class FuncoesUteis:
    """
    Essa Classe contem funções uteis para inspeção da base
    """
    @staticmethod
    def contagem_tipos_variaveis(data):
    
        col_int    = []
        col_object = []
        col_float  = []
        
        for col in data.columns:
            if data[col].dtypes =='int64':
                col_int.append(col)
            elif data[col].dtypes == 'object':
                col_object.append(col)
            elif data[col].dtypes =='float64':
                col_float.append(col)
                
        sumario = {
            'Tipo'      : ['Int', 'Float', 'Object', 'Total Colunas'], 
            'Quantidade': [len(col_int), len(col_float), len(col_object), data.shape[1]]
        }
        sumario = pd.DataFrame(sumario)
        
        return sumario , col_int, col_object, col_float
    
    @staticmethod
    def varredura_nulos(data: pd.DataFrame) -> pd.DataFrame:
        """
        Esta função faz uma varredura para contabilizar nulos, nas e conta os elementos únicos.
        
        Entrada:
        data : Dataset de trabalho 
        
        Saída:
        sumario: Dataframe contendo as informações sore contagem e percentual de nulos, nas e número de espécies únicas
        """
    
        sumario = {}
        total_linhas = len(data)
        contagem_nulos = data.isnull().sum(axis=0) # axis=0 por colunas
        percentual_nulos = (data.isnull().sum(axis=0)/len(data))*100
        
        contagem_nas = data.isna().sum(axis=0)
        percentual_nas = (data.isna().sum(axis=0)/len(data))*100
        
        unicos = data.nunique()

        sumario = {
            'total_elementos': total_linhas,
            'unicos' : unicos,
            'contagem_nulos'   : contagem_nulos,
            'percentual_nulos' : percentual_nulos,
            'contagem_nas': contagem_nas,
            'percentual_nas': percentual_nas
        }
        
        sumario = pd.DataFrame(sumario)
        final_sumario = sumario.sort_values(by=['percentual_nas'], 
                                            ascending=False)
    
        return final_sumario
    
    @staticmethod
    def remocao_variaveis_nulos(data: pd.DataFrame, valor_corte: float) -> pd.DataFrame:
        
        """
        O objetivo dessa função é remover as colunas/variáveis que apresentam um valor limite de nulos permitidos 
        
        Entrada:
        data: Dataframe completo
        valor_corte = Valor float de limite de corte
        
        Saída:        
        data_cleaned = DataFrame com as variáveis removidas

        """

        data_cleaned = data.dropna(thresh=int((1-valor_corte)*len(data)), axis=1)
        
        return data_cleaned
    
    @staticmethod
    def contagem_zeros(data: pd.DataFrame) -> pd.DataFrame:
        """ 
        Está função visa fazer uma varredura sobre a quantidade de zeros em cada variável.
        
        Entrada:
        data: Dataset completo com as variáveis 
        
        Saída:
        resumo: Dataframe contendo as informações de total, porcentagem de zeros por coluna.
        """
        total_elementos  = []
        total_zeros      = []
        percentual_zeros = []
        
        total_elementos = len(data)
        total_zeros = data.isin([0]).sum(axis=0)
        percentual_zeros = (data.isin([0]).sum(axis=0) / len(data))*100
        
        resumo = {
            'total_elementos'  : total_elementos,
            'total_zeros'      : total_zeros,
            'percentual_zeros' : percentual_zeros
        }
        
        resumo = pd.DataFrame(resumo)
        final_sumario = resumo.sort_values(by=['total_zeros'],ascending=False)
        
        return final_sumario
    
    @staticmethod 
    def remocao_variaveis_zeros(data: pd.DataFrame, valor_corte: float)->pd.DataFrame:
        """ 
        O objetivo dessa função é remover as variavéis que contenham percentual de zeros acima do valor de corte
        
        Entrada:
        data: DataFrame completo 
        
        Saída:
        data : Dataframe contendo com as variáveis removidas
        """
        limite = valor_corte * int(len(data))
        
        data_cleaned = data.loc[:, (data.eq(0).sum(axis=0) < limite)]
        
        return data_cleaned
    
    @staticmethod
    def inputar_metodo_zeros_nulos(data : pd.DataFrame, metodo: str='mean') -> pd.DataFrame:
    
        """ 
        O objetivo dessa função é inputar nos dados faltantes o método (Média, Moda ou Mediana) apropriado.
        
        Entrada:
        data : Dataframe contendo os dados completos
        metodo : 
            Esse método poder ser média, mediana ou moda sendo o método 'mean' o padrão da função.
            
        Saída:
        dataframe: Dados com as os valores inputados 
        """
        if metodo =='mean':
            return data.fillna(data.mean())
        elif metodo == 'moda':
            return data.fillna(data.mode.iloc(0))
        elif metodo =='median':
            return data.fillna(data.median())
        
        else:
            raise ValueError("Falha ao reconhecer o método! Use 'mean', 'mode' ou 'median'")
        
    @staticmethod 
    
    def remover_variaveis_um_unico_valor(data):
        """ 
        Remove as colunas que apresentam apenas um único valore repetido
        """ 
        data = data.loc[:, data.nunique() > 1]
        return data
    