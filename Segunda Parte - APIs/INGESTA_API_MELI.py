# Databricks notebook source
import requests
import json

# COMMAND ----------

url = 'https://api.mercadolibre.com/sites/MLA/search?q=chromecast&limit=50#json'
response = requests.get(url)
data=response.json()
aux=data["results"]

# COMMAND ----------

listaId = []
for item in aux:
    listaId.append(list(item.values())[0])
#print(listaId)

# COMMAND ----------

datos = []
for id in listaId:
    url = 'https://api.mercadolibre.com/items/' + id
    response = requests.get(url)
    datos.append(response.json())
    #print (response.json())

# COMMAND ----------

print (len(datos))
#print (datos[0])

# COMMAND ----------

import pandas as pd
from pandas.io.json import json_normalize
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.functions import col, struct, when
from pyspark.sql.types import StructType, StructField, IntegerType, LongType, StringType, FloatType

 

schema = StructType([StructField("id", StringType(),True),
            StructField("title",StringType(),True),
            StructField("seller_id",StringType(),True),
            StructField("category_id",StringType(),True),
            StructField("price",StringType(),True),
            StructField("base_price",StringType(),True),
            StructField("currency_id",StringType(),True),
            StructField("initial_quantity",StringType(),True),
            StructField("available_quantity",StringType(),True),
            StructField("sold_quantity",StringType(),True),
            StructField("buying_mode",StringType(),True),
            StructField("listing_type_id",StringType(),True),        
            StructField("start_time",StringType(),True),
            StructField("stop_time",StringType(),True),
            StructField("condition",StringType(),True),
            StructField("accepts_mercadopago",StringType(),True),
            StructField("international_delivery_mode",StringType(),True),
            StructField("status",StringType(),True),
            StructField("warranty",StringType(),True),
            StructField("catalog_product_id",StringType(),True),
            StructField("domain_id",StringType(),True),
            StructField("automatic_relist",StringType(),True),
            StructField("date_created",StringType(),True),
            StructField("last_updated",StringType(),True),
            StructField("health",StringType(),True),
            StructField("catalog_listing",StringType(),True)])

#dataframe1
df1 = spark.createDataFrame(datos, schema)

# COMMAND ----------

df1.display()

# COMMAND ----------

#exportar a csv
#df1.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("dbfs:/FileStore/df/df.csv")

# COMMAND ----------



# COMMAND ----------


