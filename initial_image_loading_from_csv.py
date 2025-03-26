from dotenv import load_dotenv
from psycopg2.extensions import register_adapter, AsIs
import psycopg2
import os
import numpy as np
from create_embeddings import create_image_embedding
import csv
register_adapter(np.float32, AsIs)

load_dotenv()

def addapt_numpy_array(numpy_array):
    return AsIs(tuple(numpy_array))
register_adapter(np.ndarray, addapt_numpy_array)

# Define postgresql client and database details
conn = psycopg2.connect(
        user=os.getenv("DB_USER_NAME"),
        host=os.getenv("DB_HOST_NAME"),
        port=5432,
        dbname=os.getenv("DB_NAME"))

cur = conn.cursor()

# Function to insert the uuid and url after creating embeddings into the DB
def data_insertion(id,url):
    image_embedding = create_image_embedding(url)
    id = id        
       
    cur.execute(
            "INSERT INTO public.image_search (id,url,embedding) VALUES (%s, %s, %s)",
            (id,url,image_embedding.tolist(),)
        )
    conn.commit()

# Function to open the csv file which has seed data information in csv format (id,Url)
with open('seed_data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader:
        print(line)
        data_insertion(line['id'], line['Url'])
  
cur.close()
conn.close()
        