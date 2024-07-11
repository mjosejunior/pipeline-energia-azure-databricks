# Catálogo de Dados

## Dataset: inadimplencia.csv

| Coluna                  | Descrição                            |
| :---------------------- | :----------------------------------- |
| DatGeracaoConjuntoDados | Data de geração do conjunto de dados |
| SigAgente               | Sigla do agente responsável          |
| NumCNPJ                 | Número do CNPJ do agente             |
| SigIndicador            | Sigla do indicador                   |
| AnoIndice               | Ano do índice                        |
| NumPeriodoIndice        | Número do período do índice          |
| VlrIndiceEnviado        | Valor do índice enviado              |

## Descrição detalhada

Este dataset contém informações sobre a inadimplência de consumidores de energia elétrica para as distribuidoras do Brasil. As colunas representam diferentes indicadores e períodos, fornecendo uma visão detalhada da inadimplência ao longo do tempo.

### Atributos

- **DatGeracaoConjuntoDados**: Data de geração do conjunto de dados.
  - Exemplo: 05/07/2024
- **SigAgente**: Sigla do agente responsável.
  - Exemplo: EQUATORIAL PI
- **NumCNPJ**: Número do CNPJ do agente.
  - Exemplo: 06840748000189
- **SigIndicador**: Sigla do indicador de inadimplência.
  - Exemplo: IResBR1, IResBR3
- **AnoIndice**: Ano do índice de inadimplência.
  - Exemplo: 2012
- **NumPeriodoIndice**: Número do período do índice.
  - Exemplo: 1
- **VlrIndiceEnviado**: Valor do índice enviado.
  - Exemplo: 3,54, 1,08

Este dataset é utilizado para analisar a inadimplência dos consumidores ao longo dos anos, permitindo uma análise detalhada e identificação de padrões sazonais e variações por classe de consumo.

### Observações

Os dados foram obtidos de - [Inadimplência nas Distribuidoras - Dados Abertos GOV.BR](https://dados.gov.br/dados/conjuntos-dados/indqual-inadimplencia). Eles representam dados reais disponibilizados pela Agência Nacional de Energia Elétrica - ANEEL. Os dados de inadimplência são disponibilizados pela agência para permitir a análise do aging list das distribuidoras por classe de consumo em relação à receita faturada além da quantidade de suspensões por inadimplemento.

## Dataset: dominio-indicadores.csv

| Coluna                  | Descrição                                                                                                                                                                                                                                                          | Tipo de dado         | Tamanho do campo | Valor mínimo | Valor máximo |
| :---------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------- | :--------------- | :----------- | :----------- |
| DatGeracaoConjuntoDados | Data do processamento de carga automática no momento da geração para publicação do conjunto de dados abertos                                                                                                                                                       | Data Simples         |                  |              |              |
| SigAgente               | Sigla que abrevia o nome dos Agentes regulados pela ANEEL                                                                                                                                                                                                          | Cadeia de caracteres | 20               |              |              |
| NumCNPJ                 | CNPJ do Agente do setor elétrico conforme cadastro de agentes da ANEEL                                                                                                                                                                                             | Cadeia de Caracteres | 14               |              |              |
| SigIndicador            | Sigla do Tipo de Indicador. As siglas e descrições completas das mesmas estão disponibilizadas em um arquivo à parte devido a volumetria que esses dados gerariam. Vide o arquivo dominio-indicadores.csv disponibilizado na mesma página desse conjunto de dados. | Cadeia de Caracteres | 3                |              |              |
| AnoIndice               | Ano de competência do índice                                                                                                                                                                                                                                       | Cadeia de Caracteres | 4                |              |              |
| NumPeriodoIndice        | Período do índice expressado em meses                                                                                                                                                                                                                              | Numérico             | 4                | 1            | 12           |
| VlrIndiceEnviado        | Valor do índice enviado                                                                                                                                                                                                                                            | Numérico             | 18,2             |              |              |

## Descrição detalhada

Este dataset contém informações sobre os indicadores de domínio utilizados para análise de dados específicos. As colunas representam diferentes aspectos dos indicadores, fornecendo uma visão detalhada dos dados disponíveis.

### Atributos

- **DatGeracaoConjuntoDados**: Data do processamento de carga automática no momento da geração para publicação do conjunto de dados abertos.
- **SigAgente**: Sigla que abrevia o nome dos Agentes regulados pela ANEEL.
- **NumCNPJ**: CNPJ do Agente do setor elétrico conforme cadastro de agentes da ANEEL.
- **SigIndicador**: Sigla do Tipo de Indicador. As siglas e descrições completas das mesmas estão disponibilizadas em um arquivo à parte devido a volumetria que esses dados gerariam. Vide o arquivo dominio-indicadores.csv disponibilizado na mesma página desse conjunto de dados.
- **AnoIndice**: Ano de competência do índice.
- **NumPeriodoIndice**: Período do índice expressado em meses.
- **VlrIndiceEnviado**: Valor do índice enviado.

### Observações

Os dados foram obtidos de - [Inadimplência nas Distribuidoras - Dados Abertos GOV.BR](https://dados.gov.br/dados/conjuntos-dados/indqual-inadimplencia). Eles representam dados reais disponibilizados pela Agência Nacional de Energia Elétrica - ANEEL. Os dados de inadimplência são disponibilizados pela agência para permitir a análise do aging list das distribuidoras por classe de consumo em relação à receita faturada além da quantidade de suspensões por inadimplemento.

## Dataset: taxa_desemprego.csv

| Coluna         | Descrição                            |
| :------------- | :----------------------------------- |
| DatGeracao     | Data de geração do conjunto de dados |
| Ano            | Ano da taxa de desemprego            |
| Mes            | Mês da taxa de desemprego            |
| TaxaDesemprego | Valor da taxa de desemprego          |

## Descrição detalhada

Este dataset contém informações sobre a taxa de desemprego. As colunas representam diferentes aspectos dos indicadores de desemprego, fornecendo uma visão detalhada dos dados disponíveis.

### Atributos

- **DatGeracao**: Data de geração do conjunto de dados.
- **Ano**: Ano da taxa de desemprego.
- **Mes**: Mês da taxa de desemprego.
- **TaxaDesemprego**: Valor da taxa de desemprego.

### Observações

Os dados de [Inflação (IPCA) e Taxa Desemprego - Foram obtidos do IPEA Dados Abertos GOV.BR](https://www.ipea.gov.br/cartadeconjuntura/index.php/series-estatisticas-conjunturais-2/) esses dados oferecem insights sobre os valores e a periodicidade dos mesmos.

## Dataset: inflacao_ipca.csv

| Coluna     | Descrição                                            | Tipo de dado | Valor mínimo | Valor máximo |
| :--------- | :--------------------------------------------------- | :----------- | :----------- | :----------- |
| DatGeracao | Data de geração do conjunto de dados                 | Data         |              |              |
| Ano        | Ano da inflação                                      | Inteiro      |              |              |
| Mes        | Mês da inflação                                      | Inteiro      | 1            | 12           |
| ValorIPCA  | Valor do IPCA (Índice de Preços ao Consumidor Amplo) | Decimal      |              |              |

## Descrição detalhada

Este dataset contém informações sobre o índice de preços ao consumidor amplo (IPCA). As colunas representam diferentes aspectos dos indicadores de inflação, fornecendo uma visão detalhada dos dados disponíveis.

### Atributos

- **DatGeracao**: Data de geração do conjunto de dados.
- **Ano**: Ano da inflação.
- **Mes**: Mês da inflação (valores de 1 a 12).
- **ValorIPCA**: Valor do IPCA (Índice de Preços ao Consumidor Amplo).

### Observações

Os dados de [Inflação (IPCA) e Taxa Desemprego - Foram obtidos do IPEA Dados Abertos GOV.BR](https://www.ipea.gov.br/cartadeconjuntura/index.php/series-estatisticas-conjunturais-2/) esses dados oferecem insights sobre os valores e a periodicidade dos mesmos.

## Dataset: bcdata.sgs.1207.csv

| Coluna   | Descrição                            | Tipo de dado | Valor mínimo | Valor máximo |
| :------- | :----------------------------------- | :----------- | :----------- | :----------- |
| Data     | Data de geração do conjunto de dados | Data         |              |              |
| ValorPIB | Valor do PIB                         | Decimal      |              |              |

## Descrição detalhada

Este dataset contém informações sobre o Produto Interno Bruto (PIB). As colunas representam diferentes aspectos dos indicadores econômicos, fornecendo uma visão detalhada dos dados disponíveis.

### Atributos

- **Data**: Data de geração do conjunto de dados.
- **ValorPIB**: Valor do PIB.

### Observações

Os dados do [Produto Interno Bruto (PIB) - foram obtidos de Dados Abertos GOV.BR](https://api.bcb.gov.br/dados/serie/bcdata.sgs.1207/dados?formato=csv&dataInicial=01/01/2012&dataFinal=31/05/2024). Eles representam uma amostra de indicadores utilizados para fins diversos de análise e estudo, oferecendo insights sobre os valores e a periodicidade dos mesmos.
