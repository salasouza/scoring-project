import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
import argparse
from datetime import datetime, timedelta 

from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo
# from abc import ABC, abstractmethod

class Utils:
    
    @staticmethod
    def varredura_inicial(data: pd.DataFrame) -> pd.DataFrame:
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
    def verificar_tipo_variavel(data: pd.DataFrame)->pd.DataFrame:
        """
        O objetivo dessa função é verificar qual o tipo da variável nos dados
        
        Entrada:
        data: Dataset completo
        
        Saída:
        variaveis_int: lista de variáveis do tipo int
        variaveis
        
        """
        
        variaveis_object = []
        variaveis_int = []
        variaveis_float = []
        
        for col in data.columns:
            if data[col].dtypes == 'object':
                variaveis_object.append(col)
                
            elif data[col].dtypes == 'int64':
                variaveis_int.append(col)
                
            elif data[col].dtypes =='float64':
                variaveis_float.append(col)
        
        return variaveis_object, variaveis_int, variaveis_float
    
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
    def identificao_outlier(data: pd.DataFrame) -> pd.DataFrame:
        """
        O objetivo dessa função é utilizar o método IQR (Distância Interquartilica) para remoção dos valores de outliers
        
        Entrada:
        data
        
        Saída:
        """
        
        resumo = {}
        colunas = []
        
        quartil_1 = []
        quartil_3 = []
        mediana   = []
        val_minimo = []
        val_maximo = []
        
        lim_inferior = []
        lim_superior = []
        
        for col in data.columns:
            q1 = data[col].quantile(0.25)
            q3 = data[col].quantile(0.75)
            q2 = data[col].quantile(0.5)
            val_min = data[col].min()
            val_max = data[col].max()
            
            colunas.append(col)
            quartil_1.append(q1)
            quartil_3.append(q3)
            mediana.append(q2)
            val_minimo.append(val_min)
            val_maximo.append(val_max)
            
            iqr = q3 - q1 
            
            limite_inferior = q1 - 1.5 * iqr
            limite_superior = q3 + 1.5 * iqr
            
            lim_inferior.append(limite_inferior)
            lim_superior.append(limite_superior)
            
        
        resumo = {
            'colunas' : colunas,
            'limite_inferior': lim_inferior,
            'minimo':val_minimo,
            'quartil_1' : q1,
            'mediana': mediana,
            'quartil_3' : q3,
            'maximo': val_maximo,
            'limite_superior': lim_superior
            }
        
        resumo = pd.DataFrame(resumo)
        
        return resumo
    
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
    # Função para carregar e exibir o dataset
    def carregar_dataset(caminho):
        """ 
        O objetivo dessa função é carregar o dataset.
        
        Entrada:
        data: Dataset completo
        
        Saída:
        data: Dataframe completo
        
        """
        try:
            # Supondo que o dataset seja um arquivo CSV
            dataset = pd.read_csv(caminho)
            print("Dataset carregado com sucesso!")
            print(dataset.head())  # Exibe as primeiras 5 linhas
        except Exception as e:
            print(f"Erro ao carregar o dataset: {e}")
        return dataset 
    
    @staticmethod 
    def main():
        # Configuração do argparse
        parser = argparse.ArgumentParser(description="Carregar um dataset e realizar análise.")
        parser.add_argument("caminho", 
                            type=str, 
                            help="Caminho para o arquivo CSV do dataset")
        
        # Parse dos argumentos
        args = parser.parse_args()
        
        # Carregar o dataset usando o caminho fornecido
        return Utils.carregar_dataset(args.caminho)
    
    @staticmethod
    def teste_esfericidade(data):
        """
        Esta função aplica o teste de esfericidade de Bartlett.
        
        Entrada:
        data
        
        Saída:
        bartelett:
        p_value:
        """
        
        bartlett, p_value = calculate_bartlett_sphericity(data)

        print(f'Bartlett statistic: {bartlett}')

        print(f'p-value : {p_value}')

        if p_value < 0.05:
            print('Rejeitamos a Hipótese Nula (A Matriz de correlação de Pearson não é igual a Matrix Identidade')
        else:
            print('Não Rejeitamos a Hipótese (A Matriz de correlação de Pearson é igual a Matriz Identidade')
            
        return bartlett, p_value
    
    @staticmethod
    def teste_kmo(data):
        """ 
        Esta função realizar o calcula o KMO para verificar a adequação global da Análise Fatorial
        
        Entrada:
        data: Dataframe
        
        Saida:
        
        kmo_model : float
        """
        kmo_all, kmo_model = calculate_kmo(data)
        
        if 1.0 >= kmo_model >= 0.9:
            print("Adequação Global: Muito Boa")
        elif 0.9 >= kmo_model >= 0.8:
            print('Adequação Global: Boa')
        elif 0.8 >= kmo_model >= 0.7:
            print('Adequação Global: Média')
        elif 0.7 >= kmo_model >= 0.6:
            print("Adequação Global: Razoavél")
        elif 0.6 >= kmo_model >= 0.5:
            print("Adequação Global: Má")
        else:
            print("Adequação Global: Inaceitável") 
        return kmo_all, kmo_model