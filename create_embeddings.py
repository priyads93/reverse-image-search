from PIL import Image
from sentence_transformers import SentenceTransformer, util
import requests

# Model and processor configuration
#model = SentenceTransformer('clip-ViT-B-32')
model = SentenceTransformer('clip-ViT-L-14')


# Define max width and height for resizing
MAX_WIDTH = 1024  
MAX_HEIGHT = 1024 

# Function to resize image
def resize_image(image_data):
    image = Image.open(requests.get(image_data, stream=True).raw)

    # Resize image while maintaining aspect ratio
    image.thumbnail((MAX_WIDTH, MAX_HEIGHT))
    return image

# Function to create embedding from input image
def create_image_embedding(image):
    resized_image = resize_image(image)
    img_emb = model.encode(resized_image)
    return img_emb