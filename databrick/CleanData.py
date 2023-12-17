# Databricks notebook source
dbutils.widgets.text("fileName", "hospital_admissions.csv")
fileName = dbutils.widgets.get("fileName")

spark.conf.set("fs.azure.account.key.covid19mebinsa.dfs.core.windows.net", "VFrGxhZM6xWzMlkRU9zAgW+3QQxlKBsuh6wcK2jaUmtmgSkVe3XlUyORctRwna/j52Dx0c6luoTP+AStSVwXhA==")
df = spark.read.csv("abfss://information@covid19mebinsa.dfs.core.windows.net/ECDC/"+fileName, header=True)
display(df)

# COMMAND ----------

df.write.csv("abfss://testing@covid19mebinsa.dfs.core.windows.net/ECDC/"+fileName, mode="overwrite")
