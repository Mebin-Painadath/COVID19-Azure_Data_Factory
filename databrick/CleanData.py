# Databricks notebook source
dbutils.widgets.text("fileName", "case_deaths_uk_ind_only.csv")
fileName = dbutils.widgets.get("fileName")

spark.conf.set("fs.azure.account.key.covid19mebinsa.dfs.core.windows.net", "VFrGxhZM6xWzMlkRU9zAgW+3QQxlKBsuh6wcK2jaUmtmgSkVe3XlUyORctRwna/j52Dx0c6luoTP+AStSVwXhA==")
df = spark.read.csv("abfss://information@covid19mebinsa.dfs.core.windows.net/ECDC/"+fileName, header=True)

# COMMAND ----------

from pyspark.sql.functions import when, col, regexp_replace

match fileName:
    case 'case_deaths_uk_ind_only.csv' | 'cases_deaths.csv':
        df = df.filter(df.country_code.isNotNull())
    case 'country_response.csv':
        df = df.filter(df.Response_measure.isNotNull())
    case 'country_response.csv':
        df = df.filter(df.Response_measure.isNotNull())
    case 'hospital_admissions.csv':
        df = df.filter(df.indicator.isNotNull())
        df = df.withColumn("url", when(col("url") == "\n", "").otherwise(col("url")))
    case 'testing.csv':
        df = df.filter(df.country_code.isNotNull())
        df = df.withColumn("testing_data_source", regexp_replace(col("testing_data_source"), "\n", ""))

# COMMAND ----------

df.write.option("header",True).csv("abfss://testing@covid19mebinsa.dfs.core.windows.net/Temp_ECDC/"+fileName, mode="overwrite")
