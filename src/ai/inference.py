import os
import requests

def generate_summary(text, ane_ide):
    """Genera un resumen breve con Llama 3 via Ollama."""
    if not text or len(text) < 10:
        return "Contenido insuficiente para resumen."
    
    url = os.getenv('OLLAMA_URL', 'http://localhost:11434/api/generate')
    model = os.getenv('AI_MODEL', 'llama3.1:latest')
    
    prompt = f"Resume el siguiente texto en una sola oración concisa (máximo 15 palabras): {text[:5000]}"
    try:
        res = requests.post(url, json={
            "model": model, 
            "prompt": prompt, 
            "stream": False
        }, timeout=120)
        res.raise_for_status()
        summary = res.json().get('response', '').strip()
        # Limpiar posibles prefijos de la IA
        summary = summary.replace('Resumen:', '').replace('Aquí tienes un resumen:', '').strip()
        return summary
    except Exception as e:
        error_msg = f"[ERROR] {ane_ide}: {str(e)}"
        with open("error_log.txt", "a", encoding="utf-8") as f:
            f.write(error_msg + "\n")
        return None
