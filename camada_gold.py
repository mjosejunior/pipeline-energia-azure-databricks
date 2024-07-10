# Databricks notebook source
# Databricks notebook source
# DBTITLE 1,Importação de Bibliotecas
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# DBTITLE 1,Criação da SparkSession
spark = SparkSession.builder.appName("CamadaGold").getOrCreate()

# DBTITLE 1,Carregar Dados da Camada Silver
inadimplencia_silver_df = spark.read.format('parquet').load('dbfs:/mnt/Aneel/Silver/inadimplencia_silver')
economicos_silver_df = spark.read.format('parquet').load('dbfs:/mnt/Aneel/Silver/economicos_silver')
dominio_indicadores_silver_df = spark.read.format('parquet').load('dbfs:/mnt/Aneel/Silver/dominio_indicadores_silver')

# Verificar dados carregados
display(inadimplencia_silver_df)
display(economicos_silver_df)
display(dominio_indicadores_silver_df)

# DBTITLE 1,Criar Tabelas Dimensão e Fato
# Tabela Fato de Inadimplência
fact_inadimplencia = inadimplencia_silver_df.select(
    'AnoIndice', 'SigAgente', 'SigIndicador', 'VlrIndiceEnviado', 'DatGeracaoConjuntoDados'
)
fact_inadimplencia.write.format('parquet').mode('overwrite').save('dbfs:/mnt/Aneel/Gold/fact_inadimplencia')

# Tabela Fato de Dados Econômicos
fact_economicos = economicos_silver_df.select(
    'AnoIndice', 'TaxaDesemprego', 'Inflacao', 'PIB'
)
fact_economicos.write.format('parquet').mode('overwrite').save('dbfs:/mnt/Aneel/Gold/fact_economicos')

# Tabelas Dimensão
dim_agente = inadimplencia_silver_df.select('SigAgente', 'NumCNPJ').distinct()
dim_agente.write.format('parquet').mode('overwrite').save('dbfs:/mnt/Aneel/Gold/dim_agente')

dim_indicador = dominio_indicadores_silver_df.select('SiglaIndicador', 'DescricaoIndicador').distinct()
dim_indicador.write.format('parquet').mode('overwrite').save('dbfs:/mnt/Aneel/Gold/dim_indicador')

# Dimensão Tempo usando 'AnoIndice' e 'NumPeriodoIndice'
dim_tempo = inadimplencia_silver_df.select('AnoIndice', 'NumPeriodoIndice').distinct()
dim_tempo = dim_tempo.withColumnRenamed('AnoIndice', 'Ano')
dim_tempo = dim_tempo.withColumnRenamed('NumPeriodoIndice', 'Mes')

# Calcular o trimestre a partir de 'Mes'
dim_tempo = dim_tempo.withColumn('Trimestre', 
    when(col('Mes').between(1, 3), 1)
    .when(col('Mes').between(4, 6), 2)
    .when(col('Mes').between(7, 9), 3)
    .otherwise(4)
)

dim_tempo.write.format('parquet').mode('overwrite').save('dbfs:/mnt/Aneel/Gold/dim_tempo')

# Verificar os dados da dimensão tempo
display(dim_tempo)

