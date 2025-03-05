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

### Procedimento

#### Fase de Preparação dos Dados:
1. Varredura do dataset:
Verificar se os dados tem dados faltantes, qual a quantidade, percentual em cada variável.

2. Verificar os tipos de variáveis:
Verificar se a amostra tem dados em formato int, float ou object.

3. Fazer uma estatística descritiva:
Calcular as medidas de tendências central (MTC) e as medidas de variabilidade do dataset.

4. Executar ações para lidar com dados faltantes:
4.1 Estipular um limite para remoção de colunas com =>60% de dados faltantes;
4.2 Determinar o IQR para eliminar os outliers;

5. Executar ações para lidar com colunas contendo Zeros:
5.1 Estipular um limite para remoção de colunas com => 60% de dados com zeros;
5.2 Fazer a imputação de dados baseados na média, moda ou mediana;

### Fase de Modelagem

