import requests
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def test_summarization():
    text = """
    Artificial Intelligence is transforming industries by enabling machines 
    to learn from data and make intelligent decisions. It is widely used in 
    healthcare, finance, education, and many other domains.
    """

    payload = {
        "inputs": text
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

if __name__ == "__main__":
    test_summarization()