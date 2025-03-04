import pandas as pd
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import pingouin as pg
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

class HandlePCA:
    def __init__(self, n_components=2):
        self.n_components = n_components

    def apply_pca(self, dados):
        """
        Aplica PCA nos dados normalizados.
        """
        pca = PCA(n_components=self.n_components)
        principal_components = pca.fit_transform(dados)
        
        # Cria um DataFrame com as componentes principais
        columns = [f"PC{i+1}" for i in range(self.n_components)]
        pca_df = pd.DataFrame(principal_components, columns=columns)
        
        print("PCA aplicado com sucesso!")
        return pca_df
    
    def generate_ranking(self, pca_df):
        """
        Gera o ranking baseado na primeira componente principal.
        """
        ranking = pca_df['PC1'].rank(ascending=False)  # Rank pelo PC1
        pca_df['Ranking'] = ranking
        
        print("Ranking gerado com sucesso!")
        return pca_df[['Ranking', 'PC1']]
    
    def criacao_scores(self, dados):
        scaler = MinMaxScaler(feature_range=(0,100))
        dados['Score'] = scaler.fit_transform(dados[['Ranking']])
        
        return dados
    
    def plot_scores(self, dados):
        plt.plot(dados['Score'])
        plt.title('Score do clientes')
        plt.grid(True)
        plt.show()
    
    