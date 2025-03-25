# using flask_restful 
from flask import Flask, request 
from flask_restful import Resource, Api 
from create_embeddings import create_image_embedding
from search_embeddings import search_embeddings
from dotenv import load_dotenv
from psycopg2.extensions import register_adapter, AsIs
import psycopg2
import os
import numpy as np
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


# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 

class Imageembeddings(Resource): 
  
    # corresponds to the GET request. 
    # this function is called to get similar image embeddings from database
    def get(self): 
        image_url = request.args.get('image_url')       
        response = search_embeddings(image_url,cur)
        conn.commit()
        return response
  
    # Corresponds to POST request 
    # Create Embeddings Based On The Input Image
    def post(self):           
        data = request.get_json() 
        image_embedding = create_image_embedding(data['url'])
        id = data['id']        
       
        cur.execute(
                "INSERT INTO public.image_search (id,url,embedding) VALUES (%s, %s, %s)",
                (id,data['url'],image_embedding.tolist(),)
            )
        conn.commit()
        
        response={ 
            "id": data['id'],  
            "response": "Created Embeddings"
        } 
        return response
    
# adding the defined resources along with their corresponding urls 
api.add_resource(Imageembeddings, '/') 


# driver function 
if __name__ == '__main__':   
    app.run(debug = True) 