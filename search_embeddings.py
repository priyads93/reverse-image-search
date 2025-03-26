import json
from create_embeddings import create_image_embedding


def search_embeddings(image:str,cur):
    search_image_embedding = create_image_embedding(image)   
   
    
    cur.execute(
            """SELECT id,url, 1 - (embedding <=> %s) AS cosine_similarity
               FROM image_search_l14
               ORDER BY cosine_similarity DESC LIMIT 6""",
            (json.dumps(search_image_embedding.tolist()),)
        )
    
    final_response = cur.fetchall()
    
    return final_response