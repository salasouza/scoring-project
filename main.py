from carregamento_dados import CarregadorCSV
from limpeza_dados import AplicacoesLimpeza
from processamento_dados import TestesAdequacao, Preprocessamento
from modelagem_dados import HandlePCA

def main():
    
    #PARAMETROS:
    VALOR_CORTE = 0.8
    METODO = 'mean'
    features = ['Target','Id_cliente','leads_corretor_count']
    
    # Fase de Carregamento:
    
    carregador = CarregadorCSV(caminho_dados='storage/raw/sample.csv')
    dados = carregador.carregador_dados()
    
    X = dados[dados['Target'] == 0]
    dados = X.drop(columns=features)
    
    if dados is None:
        print('Falha ao carregar os dados oela função main()')
    else:
        print("Dados entraram corretamento no processo!")
    
    # Fase de Limpeza 
    acoes_limpeza = AplicacoesLimpeza()
    dados_numericos = acoes_limpeza.remover_variaveis_int_object(dados=dados)
    if dados_numericos is None:
        print('Falha ao gerar os dados_numericos')
    else:
        print('Dados Numéricos concluídos!')
        
    dados_sem_nulos = acoes_limpeza.remover_variaveis_nulos(dados=dados_numericos, valor_corte=VALOR_CORTE)
    if dados_sem_nulos is None:
        print('Falha ao gerar os dados_sem_nulos')
    else:
        print("Dados sem nulos concluído!")
        
    dados_limpos = acoes_limpeza.remover_variaveis_zeros(dados=dados_sem_nulos, valor_corte=VALOR_CORTE)
    if dados_limpos is None:
        print('Falha ao gerar os dados_limpos')
    else:
        print('Dados sem zeros concluídos!')
        
    dados_resumo = acoes_limpeza.imputar_metodo_zeros_nulos(dados=dados_limpos)
    if dados_resumo is None:
        print('Falha ao gerar os dados_resumo')
    else:
        print('Dados pronto para uso concluído!')
    
    print()
    print("[DONE]")
    print('...')
    print(dados_resumo)
    print()
    print(dados_resumo.describe().T)
    print()
    
    # Fase de Processamento dos dados
    
    adequacao_global = TestesAdequacao()
    bartlett, pvalue = adequacao_global.teste_esfericidade(dados=dados_resumo)
    
    kmo_model = adequacao_global.teste_kmo(dados=dados_resumo)
    print(f"KMO_MODEL : {kmo_model}")
    print()
    
    if pvalue < 0.05:
        print("Os dados seguem uma Adequação Global para uma Análise Fatorial")
        print()
        
        normalizador = Preprocessamento()
        dados_padronizados = normalizador.padronizacao(dados=dados_resumo)
        
        print("Dados Padronizados!")
        print("---")
        print(dados_padronizados)
        print()
        
        # Processo de Modelagem 
        motor_pca = HandlePCA()
        resultado = motor_pca.apply_pca(dados=dados_padronizados)
        
        resultado = motor_pca.generate_ranking(pca_df=resultado)
        print("RESULTADO FINAL")
        print("---")
        print(resultado)
        print()
        
        scores = motor_pca.criacao_scores(dados=resultado)
        
        print("RESULTADO FINAL")
        print("---")
        print(scores)
        print()
        motor_pca.plot_scores(dados=scores)
        
        
    else:
        print("Os dados não seguem uma Adequação Global para uma Análise Fatorial")
        
        
    

if __name__ == "__main__":
    main()