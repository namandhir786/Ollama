# run different llm from sentence transforms running on your local machine

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

sentences = ["Machine learning is amazing!", "Python is great for data science."]
embeddings = model.encode(sentences)

print(embeddings.shape)
print(embeddings[0][:10]) 



# use a small llm from hugging face running on your local (using transformers)
from transformers import AutoTokenizer, AutoModel
import torch

model_name = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

sentences = ["Machine learning is amazing!", "Python is great for data science."]

inputs = tokenizer(sentences, return_tensors='pt', padding=True, truncation=True)

with torch.no_grad():
    outputs = model(**inputs)

embeddings = outputs.last_hidden_state.mean(dim=1)
print(embeddings.shape)
print(embeddings[0][:10])



# use a llm using hugging face inference provider (use api key and request module).

import os
import requests
from dotenv import load_dotenv  

load_dotenv()

api_key = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/google/embeddinggemma-300m"
headers = {
    "Authorization": f"Bearer {api_key}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": {
        "source_sentence": "That is a happy person",
        "sentences": [
            "That is a happy dog",
            "That is a very happy person",
            "Today is a sunny day"
        ]
    }
})

print(output)

