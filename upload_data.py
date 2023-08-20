
from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://shubham:shubham@cluster0.oev8htd.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME='ML_Project'
COLLECTION_NAME='wafer_fault'

# read data as an dataframe
df=pd.read_csv("D:\ML_Projects\sensor-fault-detection\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)

#convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

