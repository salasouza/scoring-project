import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo
from abc import ABC, abstractmethod

class Processador(ABC):
    """
    Classe construida para as funções de processamento e testes estatisticos dos dados
    """

class TestesAdequacao(Processador):
    """
    Executa as funções para testes de Adequação dos dados a análise Fatorial
    """
    
    def teste_esfericidade(self, dados):
        """
        Esta função aplica o teste de esfericidade de Bartlett.
        
        Entrada:
        dados
        
        Saída:
        bartelett:
        p_value:
        """
        
        bartlett, p_value = calculate_bartlett_sphericity(dados)

        print(f'Bartlett statistic: {bartlett}')

        print(f'p-value : {p_value}')

        if p_value < 0.05:
            print('Rejeitamos a Hipótese Nula (A Matriz de correlação de Pearson não é igual a Matrix Identidade')
            print()
        else:
            print('Não Rejeitamos a Hipótese (A Matriz de correlação de Pearson é igual a Matriz Identidade')
            print()
            
        return bartlett, p_value
    
    def teste_kmo(self, dados):
        """ 
        Esta função realizar o calcula o KMO para verificar a adequação global da Análise Fatorial
        
        Entrada:
        dados: dadosframe
        
        Saida:
        
        kmo_model : float
        """
        kmo_all, kmo_model = calculate_kmo(dados)
        
        if 1.0 >= kmo_model >= 0.9:
            print("Adequação Global KMO: Muito Boa")
        elif 0.9 >= kmo_model >= 0.8:
            print('Adequação Global KMO: Boa')
        elif 0.8 >= kmo_model >= 0.7:
            print('Adequação Global KMO: Média')
        elif 0.7 >= kmo_model >= 0.6:
            print("Adequação Global KMO: Razoavél")
        elif 0.6 >= kmo_model >= 0.5:
            print("Adequação Global KMO: Má")
        else:
            print("Adequação Global KMO: Inaceitável") 
        print()
        return kmo_all, kmo_model
    

class Preprocessamento(Processador):
    """
    Funções para preprocessamento dos dados 
    """
    def padronizacao(self, dados):
        scaler = StandardScaler()
        dados_padronizados = scaler.fit_transform(dados)
        dados_padronizados = pd.DataFrame(dados_padronizados)
        
        return dados_padronizados
    