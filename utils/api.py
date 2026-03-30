import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

HEADERS = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}"
}



def split_text(text, chunk_size=100):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]


def summarize_text(text, summary_type):

    if len(text.split()) < 10:
        return "Input too short for summarization."

    chunks = split_text(text)
    summaries = []

    
    if summary_type == "Short":
        max_len = 60
        min_len = 20
    elif summary_type == "Medium":
        max_len = 100
        min_len = 30
    else: 
        max_len = 150
        min_len = 50

    for chunk in chunks:

        payload = {
            "inputs": f"Summarize the following text in your own words without copying sentences:\n\n{chunk}",
            "parameters": {
                "max_length": max_len,
                "min_length": min_len,
                "do_sample": False
            }
        }

        for attempt in range(3):
            try:
                response = requests.post(
                    API_URL,
                    headers=HEADERS,
                    json=payload,
                    timeout=20
                )

                if response is None or response.status_code != 200:
                    break
                else:
                    time.sleep(2)

            except requests.exceptions.ReadTimeout:
                time.sleep(2)

        if response.status_code != 200:
            summaries.append("")
            continue

        try:
            result = response.json()
            summaries.append(result[0]["summary_text"])
        except:
            summaries.append("")

    final_summary = " ".join(summaries).strip()

    if not final_summary:
        return "Failed to generate summary. Please try again."

    #Second pass: refine summary
    refine_payload = {
    "inputs": f"""
        Rewrite the following content into a well-structured, fully paraphrased explanation.

        - Do NOT copy sentences directly
        - Combine ideas smoothly
        - Make it sound natural and human-written
        - Keep all important information

        Text:
        {final_summary}
        """,
            "parameters": {
            "max_length": int(max_len * 1.5),
            "min_length": min_len,
            "do_sample": True,
            "temperature": 0.9,
            "top_p": 0.95
            }
    }
    
    response = None

    for attempt in range(3):
        try:
            response = requests.post(
                API_URL,
                headers=HEADERS,
                json=refine_payload,
                timeout=20
            )

            if response is not None and response.status_code == 200:
                result = response.json()
                return result[0]["summary_text"]
            else:
                time.sleep(2)

        except requests.exceptions.ReadTimeout:
            time.sleep(2)

       
    return final_summary