# Databricks notebook source
# Databricks notebook source
# DBTITLE 1,Importação de Bibliotecas
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, year, month, quarter, to_date

# DBTITLE 1,Criação da SparkSession
spark = SparkSession.builder.appName("CamadaSilver").getOrCreate()

# DBTITLE 1,Carregar Dados da Camada Bronze
inadimplencia_bronze_df = spark.read.option("delimiter", ";").csv('dbfs:/mnt/Aneel/Bronze/inadimplencia.csv', header=True, inferSchema=True)
desemprego_bronze_df = spark.read.option("delimiter", ";").csv('dbfs:/mnt/Aneel/Bronze/taxa_desemprego.csv', header=True, inferSchema=True)
pib_bronze_df = spark.read.option("delimiter", ";").csv('dbfs:/mnt/Aneel/Bronze/pib_bcdata.sgs.1207.csv', header=True, inferSchema=True)
inflacao_bronze_df = spark.read.option("delimiter", ";").csv('dbfs:/mnt/Aneel/Bronze/inflacao_ipca.csv', header=True, inferSchema=True)
dominio_indicadores_bronze_df = spark.read.option("delimiter", ",").csv('dbfs:/mnt/Aneel/Bronze/dominio-indicadores.csv', header=True, inferSchema=True)

# DBTITLE 1,Verificar Dados Carregados na Camada Bronze
display(inadimplencia_bronze_df)
display(desemprego_bronze_df)
display(pib_bronze_df)
display(inflacao_bronze_df)

# DBTITLE 1,Renomear e Limpar Colunas de Dados Econômicos
# Ajustar as tabelas de dados econômicos para garantir que todas possuam a coluna 'AnoIndice'
desemprego_bronze_df = desemprego_bronze_df.withColumnRenamed('Ano', 'AnoIndice').withColumnRenamed('Media', 'TaxaDesemprego')
pib_bronze_df = pib_bronze_df.withColumnRenamed('Data', 'AnoIndice').withColumnRenamed('valor', 'PIB')
inflacao_bronze_df = inflacao_bronze_df.withColumnRenamed('Ano', 'AnoIndice').withColumnRenamed('Media', 'Inflacao')

# Ajustar o formato da coluna AnoIndice na tabela de PIB
pib_bronze_df = pib_bronze_df.withColumn('AnoIndice', year(to_date(col('AnoIndice'), 'dd/MM/yyyy')))

# Limpar os dados para remover possíveis caracteres que possam impedir a conversão para float
desemprego_bronze_df = desemprego_bronze_df.withColumn("TaxaDesemprego", regexp_replace(col("TaxaDesemprego"), ",", "."))
pib_bronze_df = pib_bronze_df.withColumn("PIB", regexp_replace(col("PIB"), ",", "."))
inflacao_bronze_df = inflacao_bronze_df.withColumn("Inflacao", regexp_replace(col("Inflacao"), ",", "."))

# Converter colunas de string para float
desemprego_bronze_df = desemprego_bronze_df.withColumn("TaxaDesemprego", col("TaxaDesemprego").cast("float"))
pib_bronze_df = pib_bronze_df.withColumn("PIB", col("PIB").cast("float"))
inflacao_bronze_df = inflacao_bronze_df.withColumn("Inflacao", col("Inflacao").cast("float"))

# Verificar as colunas renomeadas e convertidas
display(desemprego_bronze_df)
display(pib_bronze_df)
display(inflacao_bronze_df)

# Ajuste dos Dados de Inadimplência
inadimplencia_bronze_df = inadimplencia_bronze_df.withColumn("VlrIndiceEnviado", regexp_replace(col("VlrIndiceEnviado"), ",", "."))

# Converter VlrIndiceEnviado para float
inadimplencia_bronze_df = inadimplencia_bronze_df.withColumn("VlrIndiceEnviado", col("VlrIndiceEnviado").cast("float"))

# Converter DatGeracaoConjuntoDados para data
inadimplencia_bronze_df = inadimplencia_bronze_df.withColumn("DatGeracaoConjuntoDados", to_date(col("DatGeracaoConjuntoDados"), 'dd-MM-yyyy'))

# Verificar os dados ajustados de inadimplência
display(inadimplencia_bronze_df)

# DBTITLE 1,Selecionar e Transformar Dados de Inadimplência para a Camada Silver
inadimplencia_silver_df = inadimplencia_bronze_df.select(
    'DatGeracaoConjuntoDados', 'SigAgente', 'NumCNPJ', 'SigIndicador', 'AnoIndice', 'NumPeriodoIndice', 'VlrIndiceEnviado'
)

# Verificar os dados ajustados de inadimplência na camada Silver
display(inadimplencia_silver_df)

# DBTITLE 1,Realizar a Junção das Tabelas Econômicas
economicos_silver_df = (desemprego_bronze_df
    .join(pib_bronze_df, 'AnoIndice')
    .join(inflacao_bronze_df, 'AnoIndice')
    .select('AnoIndice', 'TaxaDesemprego', 'Inflacao', 'PIB'))

# Verificar os dados da junção
display(economicos_silver_df)

# DBTITLE 1,Selecionar e Transformar Dados de Domínio de Indicadores
dominio_indicadores_silver_df = dominio_indicadores_bronze_df.select(
    'SigIndicador', 'DscIndicador'
)
# Renomear colunas
dominio_indicadores_silver_df = dominio_indicadores_silver_df.withColumnRenamed('SigIndicador', 'SiglaIndicador').withColumnRenamed('DscIndicador', 'DescricaoIndicador')

# Verificar se os caracteres acentuados foram removidos
display(dominio_indicadores_silver_df)

# DBTITLE 1,Salvar Dados Transformados na Camada Silver
# Verificar os dados antes de salvar
display(inadimplencia_silver_df)
display(economicos_silver_df)
display(dominio_indicadores_silver_df)

# Salvar dados diretamente no local correto
inadimplencia_silver_df.write.format('parquet').mode('overwrite').save('dbfs:/mnt/Aneel/Silver/inadimplencia_silver')
economicos_silver_df.write.format('parquet').mode('overwrite').save('dbfs:/mnt/Aneel/Silver/economicos_silver')
dominio_indicadores_silver_df.write.format('parquet').mode('overwrite').save('dbfs:/mnt/Aneel/Silver/dominio_indicadores_silver')

# Verificar os dados após salvar
display(spark.read.format('parquet').load('dbfs:/mnt/Aneel/Silver/inadimplencia_silver'))
display(spark.read.format('parquet').load('dbfs:/mnt/Aneel/Silver/economicos_silver'))
display(spark.read.format('parquet').load('dbfs:/mnt/Aneel/Silver/dominio_indicadores_silver'))
