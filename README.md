# Previsão do Preço de Fechamento das Ações do Google (GOOGL)
Este projeto tem como objetivo prever o preço de fechamento das ações da Google (ticker GOOGL) utilizando dados históricos de preços de abertura, maior e menor valor durante o dia e volume de negociações.

### Visão Geral
A previsão do preço de fechamento de ações é um desafio comum em finanças e aprendizado de máquina. Este projeto explora a aplicação de modelos preditivos para analisar a relação entre os preços entrada e o volume de negociações para estimar o valor de fechamento de uma ação.

### Dados
Os dados utilizados para treinar e avaliar os modelos incluem as seguintes features para cada dia de negociação:

- Preço de Abertura (Open): O preço pelo qual a ação começou a ser negociada no dia.
- Maior Valor (High): O preço máximo atingido pela ação durante o dia.
- Menor Valor (Low): O preço mínimo atingido pela ação durante o dia.
- Volume (Volume): O número total de ações negociadas durante o dia.
- Preço de Fechamento (Close): O preço pelo qual a ação fechou no dia (variável alvo).  

### Modelo Utilizado:

- Random Forest Regressor

### Como executar:

- Instale o python na versão 3.11
- bibliotecas : pandas,numpy,sklearn,matplotlib,joblib

### Estrutura do Projeto: 
- googleprices.csv : CSV para armazenar os dados brutos.
- notebooks: Contém notebooks Jupyter para exploração de dados, engenharia de features e treinamento de modelos.
- Metricas:
  
![Screenshot from 2025-06-06 15-19-09](https://github.com/user-attachments/assets/b19f108f-d7f9-4016-a51b-248fc7ddf302)

- scatter plot:

  ![Screenshot from 2025-06-06 15-22-11](https://github.com/user-attachments/assets/3c1bf6dc-a582-46af-a2fc-f9569f0ba9ac)

- Interface (usando Streamlit):

  ![Screenshot from 2025-06-06 15-23-16](https://github.com/user-attachments/assets/aeb0402f-773a-47dc-a4d9-4050070f76c7)
