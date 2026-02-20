import requests

url = "http://localhost:11434/api/generate"
# Probamos con llama3.1:latest que es el que vimos en api/tags
payload = {
    "model": "llama3.1:latest",
    "prompt": "Di hola en una palabra",
    "stream": False
}

try:
    print(f"Probando URL: {url}")
    print(f"Payload: {payload}")
    res = requests.post(url, json=payload, timeout=10)
    print(f"Status: {res.status_code}")
    print(f"Response: {res.text}")
except Exception as e:
    print(f"Error: {e}")
