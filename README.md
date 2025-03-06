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

### Estrutura do projeto:

```
.
├── storage
│   ├── raw
│   │   └── sample.csv
│   ├── processed
│   │   ├── dados.csv
│   │   ├── dados_resumo.csv
│   │   ├── dados_median.csv
│   │   ├── dados_mode.csv
│   │   └── dados_mean.csv
│   └── trusted
│       ├── data_final.csv
│       └── dados_pad.csv
├── README.md
├── funcoes_uteis.py
├── notebooks
│   ├── AnaliseExploratoria.ipynb
│   ├── Preprocessamento.ipynb
│   ├── Scoring.ipynb
│   ├── AnaliseExploratoria.html
│   ├── Preprocessamento.html
│   └── Scoring.html
└── scripts
    ├── __init__.py
    ├── carregamento_dados.py
    ├── limpeza_dados.py
    ├── main.py
    ├── modelagem_dados.py
    └── processamento_dados.py
```

#### Instruções sobre o projeto
O projeto tem dois formatos:

**(A.) Notebooks para visualização dos detalhes**
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

### Procedimento

#### Fase de Preparação dos Dados:
1. Varredura do dataset:
Verificar se os dados tem dados faltantes, qual a quantidade, percentual em cada variável.

2. Verificar os tipos de variáveis:
Verificar se a amostra tem dados em formato int, float ou object.

3. Fazer uma estatística descritiva:
Calcular as medidas de tendências central (MTC) e as medidas de variabilidade do dataset.

4. Executar ações para lidar com dados faltantes e com zeros:

    4.1 Estipular um limite para remoção de colunas com =>40% de dados faltantes ou zeros;

    4.2 Fazer a imputação de dados baseados na média, moda ou mediana;

    4.3 Elimintar as colunas com valores repetidos em 100% das vezes

5. Padronizar os dados:

    5.1 Utilizar a padronização z-score:

    $$z = \frac{x - \mu}{\sigma}$$

    Onde o:
    $x$ é o valor original,
    $\mu$ é a média dos dados,
    $\sigma$ é o desvio padrão dos dados.

#### Fase de Modelagem:
1. Identificar o tipo de tarefa: 
    O estudo é uma tarefa de classificação e foi utilizado uma técnica de Machine Learning não Supervisionado.
2. Para criar o score com base das variáveis descritivas foi utilizado a Análise Fatorial utilizando Componentes Principais para redução dimensional e utilizar um dos fatores para construir o Score para cada Id do Cliente.





