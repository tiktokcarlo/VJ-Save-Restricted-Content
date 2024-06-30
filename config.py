import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6756848818:AAGbtf_uqq_WlPHHXV1-kwOuFnhZ3Mbs8A0")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "5636761596"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8cfe8acc2e29c1dcedb2a5baa9e58f8b")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Carlo:carlohere@cluster0.ovnoi6e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
