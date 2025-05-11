from fastapi import FastAPI, HTTPException
import requests
import os

app = FastAPI()

# Set the Gemini API URL and API key (you will need to set the key securely)
GEMINI_API_URL = "https://api.gemini.com/v1/completions"  # Replace with actual Gemini API URL
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # You can set your Gemini API key in environment variables

# Function to forward the request to the Gemini API
def forward_to_gemini(prompt: str):
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "max_tokens": 100  # You can adjust the number of tokens based on your requirements
    }
    
    # Send the request to Gemini API
    response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the successful response
    else:
        raise HTTPException(status_code=response.status_code, detail="Error contacting Gemini API")

@app.post("/proxy")
async def proxy_request(prompt: str):
    """
    This is the main endpoint for the proxy API.
    Users will send a prompt, and the API will forward the request to the Gemini API.
    """
    return forward_to_gemini(prompt)
