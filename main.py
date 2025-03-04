from carregamento_dados import CarregadorCSV
from limpeza_dados import AplicacoesLimpeza

def main():
    
    #PARAMETROS:
    VALOR_CORTE = 0.8
    METODO = 'mean'
    features = ['Target','Id_cliente']
    
    # Fase de Carregamento
    carregador = CarregadorCSV(caminho_dados='storage/raw/sample.csv')
    dados = carregador.carregador_dados()
    
    dados = dados.drop(columns=features)
    
    if dados is None:
        print('Falha ao carregar os dados oela função main()')
    print("[DADOS DE ENTRADA]")
    print(dados)
    
    # Fase de Limpeza 
    acoes_limpeza = AplicacoesLimpeza()
    dados_numericos = acoes_limpeza.remover_variaveis_int_object(dados=dados)
    if dados_numericos is None:
        print('Falha ao gerar os dados_numericos')
    else:
        print(dados_numericos)
        
    dados_sem_nulos = acoes_limpeza.remover_variaveis_nulos(dados=dados_numericos, valor_corte=VALOR_CORTE)
    if dados_sem_nulos is None:
        print('Falha ao gerar os dados_sem_nulos')
    else:
        print(dados_sem_nulos)
        
    dados_limpos = acoes_limpeza.remover_variaveis_zeros(dados=dados_sem_nulos, valor_corte=VALOR_CORTE)
    if dados_limpos is None:
        print('Falha ao gerar os dados_limpos')
    else:
        print(dados_limpos)
        
    dados_resumo = acoes_limpeza.imputar_metodo_zeros_nulos(dados=dados_limpos)
    
    print()
    print("[DONE]")
    print('...')
    print(dados_resumo)
    
    print(dados_resumo.describe().T)
    
    

if __name__ == "__main__":
    main()