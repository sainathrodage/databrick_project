# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers
# MAGIC 1. raw
# MAGIC 2. processed
# MAGIC 3. lookup

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "0c57c7f2-12da-47c2-9e0b-5f746ee9a3a0",
           "fs.azure.account.oauth2.client.secret": "N.V8Q~2zYmEuBn8YnvoT1GmQ62RSVCuuI1BF-aJF",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/7b1adf98-ba9e-4c5a-8db5-dfae3f3c9f1b/oauth2/token"}

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://raw@adlsproject.dfs.core.windows.net/",
  mount_point = "/mnt/adlsproject/raw",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the processed container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://processed@adlsproject.dfs.core.windows.net/",
  mount_point = "/mnt/adlsproject/processed",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the lookup container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://lookup@adlsproject.dfs.core.windows.net/",
  mount_point = "/mnt/adlsproject/lookup",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/adlsproject/processed")
