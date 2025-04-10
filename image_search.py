from PIL import Image
from sentence_transformers import SentenceTransformer, util
import chromadb
import os
from pathlib import Path

# Model and processor configuration
model = SentenceTransformer('clip-ViT-B-16')

# Define chroma client and collection details
chroma_client = chromadb.HttpClient(host='localhost', port=8000)
collection = chroma_client.get_or_create_collection(name="image_collections_v2")  

# Define max width and height for resizing
MAX_WIDTH = 1024  
MAX_HEIGHT = 1024 

# Function to resize image
def resize_image(image_data):
    image = Image.open(image_data)

    # Resize image while maintaining aspect ratio
    image.thumbnail((MAX_WIDTH, MAX_HEIGHT))
    return image

# Function to create embedding from input image
def create_image_embedding(image):
    img_emb = model.encode(image)
    return img_emb


dirname = os.path.dirname(__file__)
path = os.path.join(dirname, "images/")
dir_list = os.listdir(path)

contents = list(map(lambda file_name: f"{path}{file_name}",dir_list))


# Loop through contents array to encode each image, generate its embedding, and append to array
for obj in contents:
    # Resize the image to meet model requirements
    resized_image = resize_image(obj)    

    # Generate the embedding for the resized image
    image_embedding = create_image_embedding(resized_image)
    collection.upsert(ids=[Path(obj).stem],embeddings=[image_embedding])


def handler():
    searchImage = os.path.join(dirname,"searchImages","verify.jpg")
    # Resize the image to meet model requirements
    resized_image = resize_image(searchImage)

    # Generate the embedding for the resized image    
    search_image_embedding = create_image_embedding(resized_image)
    final_response = collection.query(
        query_embeddings=[search_image_embedding],
        n_results=4,
        include=["distances"]
    )
    print(final_response)

handler()







