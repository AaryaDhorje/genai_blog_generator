import re
import requests
import os
from collections import Counter

def summarize_text(text):
    hf_api_key = os.getenv("HF_API_KEY")
    url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {hf_api_key}"}
    payload = {"inputs": text}

    response = requests.post(url, headers=headers, json=payload)
    if response.ok:
        return response.json()[0]['summary_text']
    else:
        return "Summary not available."

def extract_keywords(text):
    words = re.findall(r'\w+', text.lower())
    common_words = Counter(words).most_common(20)
    return [word for word, count in common_words if len(word) > 4]
