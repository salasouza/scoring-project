# Desafio Técnico

### Case Técnico: Modelagem de Scoring para Classificação de Clientes</b>
Você foi contratado por uma empresa para desenvolver um modelo de scoring de clientes e esta empresa lhe forneceu uma amostra.
Nessa amostra existem clientes já “scorados” /qualificados e clientes que precisam ser ”scorados”/qualificados.

### Sobre os dados:

Clique aqui para conferir a amostra de dados. Amostra de dados contendo diversas variáveis sobre os clientes.
Coluna alvo (target): indica se o cliente já foi qualificado (1) ou não (0).

### Desafio

Construa um modelo capaz de atribuir um score de 0 a 100 aos clientes que possuem a coluna (target) = 0.
Explique detalhadamente o processo de construção do modelo.

### Avaliação

Será considerada a qualidade do código e a clareza da explicação da análise realizada.

Estrutura do projeto:

```
├── README.md
├── __init__.py
├── carregamento_dados.py 
├── processamento_dados.py
├── storage
│   ├── raw
│   │   └── sample.csv       # Arquivo Original de Trabalho
│   ├── processed
│   │   ├── dados.csv       
│   │   ├── dados_resumo.csv
│   │   ├── dados_median.csv
│   │   ├── dados_mode.csv  
│   │   └── dados_mean.csv  
│   └── trusted
│       ├── data_final.csv
│       └── dados_pad.csv 
├── modelagem_dados.py
├── requeriments.txt
├── AnaliseExploratoria.ipynb
├── Preprocessamento.ipynb
├── funcoes_uteis.py
├── Scoring.ipynb
├── main.py                   
├── limpeza_dados.py
```

#### Instruções sobre o projeto
O projeto tem duas estruturas uma em notebooks.ipynb para visualização passo a passo:

**(A.) Parte de Notebooks para visualização dos detalhes**
1. AnaliseExploratoria.ipynb 
2. Preprocessamento.ipynb 
3. Scoring.ipynb 
4. funcoes_uteis.py  --> Arquivo contendo funções para uso no processo

**(B.) Protótipo de um motor para scoring**
1. carregamento_dados.py
2. limpeza_dados.py
2. processamento_dados.py
3. modelagem_dados.py 
4. main.py  --> Arquivo central para execução






