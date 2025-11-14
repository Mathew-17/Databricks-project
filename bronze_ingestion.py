# Databricks notebook source
 df = spark.read.format("csv")\
    .option("header", True)\
    .option("inferSchema", True)\
    .load("/Volumes/pysparkdbt/source/source_data/customers/")


# COMMAND ----------

display(df)

# COMMAND ----------

df.schema

# COMMAND ----------

# MAGIC %md
# MAGIC ### "SPARK STRAMING"

# COMMAND ----------

entities = ["customers", "drivers", "trips", "location","payments","vehicles"]

# COMMAND ----------

for entity in entities:
    df_batch = spark.read.format("csv")\
    .option("header", True)\
    .option("inferSchema", True)\
    .load(f"/Volumes/pysparkdbt/source/source_data/{entity}/")

    schema_entity = df_batch.schema

    df = spark.readStream.format("csv")\
        .option("header", True)\
        .schema(schema_entity)\
        .load(f"/Volumes/pysparkdbt/source/source_data/{entity}/")

    df.writeStream.format("delta")\
        .outputMode("append")\
        .option("checkpointLocation",f"/Volumes/pysparkdbt/bronze/checkpoint/{entity}")\
        .trigger(once=True)\
        .toTable(f"pysparkdbt.bronze.{entity}")



# COMMAND ----------

