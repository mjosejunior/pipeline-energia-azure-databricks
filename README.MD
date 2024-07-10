## Objetivo

O objetivo deste projeto é analisar a inadimplência dos consumidores das distribuidoras de energia elétrica ao longo dos anos, suas correlações com indicadores econômicos, variações por classe de consumo, e identificar padrões sazonais.

## Perguntas a Serem Respondidas

Como a inadimplência varia por classe de consumo nos anos de 2021 e 2022?
Qual é a correlação entre inadimplência e indicadores econômicos?
Qual é a tendência geral da inadimplência ao longo dos anos?
Qual é a análise sazonal da inadimplência?
Qual é a performance das distribuidoras em relação à inadimplência (Top 10)?
Qual é a análise de inadimplência durante a pandemia (2021-2022)?

## Descrição

Este repositório contém o projeto MVP do curso de Engenharia de Dados, focado na análise de inadimplência dos consumidores das distribuidoras de energia elétrica utilizando as plataformas Azure e Databricks. O objetivo principal é entender as variações de inadimplência ao longo dos anos, suas correlações com indicadores econômicos, variações por classe de consumo, e identificar padrões sazonais.

## Estrutura do Projeto

### Camada Bronze

Armazenamento dos dados brutos extraídos de diversas fontes, mantendo-os em seu formato original.

### Camada Silver

Nesta camada, os dados da camada Bronze são limpos e transformados, aplicando regras de qualidade e padronização.

### Camada Gold

Dados refinados e integrados para análises e visualizações. Tabelas de fato e dimensões são criadas usando o esquema estrela.

## Fontes de Dados

- [Inadimplência nas Distribuidoras - Dados Abertos GOV.BR](https://dados.gov.br/dados/conjuntos-dados/indqual-inadimplencia)

- [Produto Interno Bruto (PIB) - Dados Abertos GOV.BR](https://api.bcb.gov.br/dados/serie/bcdata.sgs.1207/dados?formato=csv&dataInicial=01/01/2012&dataFinal=31/05/2024)

- [Inflação (IPCA) e Taxa Desemprego - IPEA Dados Abertos GOV.BR](https://www.ipea.gov.br/cartadeconjuntura/index.php/series-estatisticas-conjunturais-2/)

## Cluster configurado

### ![Cluster Databricks](imagens/cluster_databricks.png)

## Diagramas

### Arquitetura da Solução

### ![Diagrama de Arquitetura](diagramas/arquitetura/diagrama.svg)

### Esquema Estrela

### ![Diagrama tabelas Fato e Dimensões](diagramas/schema/Diagrama.svg)

## Pipeline

### ![Pipeline](imagens/pipeline.png)

### ![Pipeline](imagens/pipeline_trigger.png)

## Camadas (Bronze, Silver, Gold)

### ![Camadas](imagens/camadas.png)

## Bronze

### ![Dados Bronze](imagens/cm_bronze.png)

## Silver

### ![Silver](imagens/cm_silver.png)

### ![Silver](imagens/parquet_silver.png)

## Gold

### ![Gold](imagens/cm_gold.png)

### ![Gold](imagens/parquet_gold.png)

## Analises

## Pergunta 1: Como a inadimplência varia por classe de consumo nos anos de 2021 e 2022?

### ![Pergunta 1](imagens/1.png)

## Pergunta 2: Qual é a correlação entre inadimplência e indicadores econômicos?

### ![Pergunta 2](imagens/2.png)

### ![Pergunta 2](imagens/2.1.png)

### ![Pergunta 2](imagens/2.2.png)

## Pergunta 3: Qual é a tendência geral da inadimplência ao longo dos anos?

### ![Pergunta 3](imagens/3.png)

## Pergunta 4: Análise sazonal da inadimplência

### ![Pergunta 4](imagens/4.png)

## Pergunta 5: Qual é a performance das distribuidoras em relação à inadimplência (Top 10)?

### ![Pergunta 5](imagens/5.png)

## Pergunta 6: Qual é a análise de inadimplência durante a pandemia (2021-2022)?

### ![Pergunta 6](imagens/6.png)

### ![Pergunta 6](imagens/6.1.png)
