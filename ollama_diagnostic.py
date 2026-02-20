import requests

def diagnostic():
    url_tags = "http://localhost:11434/api/tags"
    try:
        res = requests.get(url_tags)
        print(f"Status Tags: {res.status_code}")
        models = res.json().get('models', [])
        print(f"Modelos encontrados ({len(models)}):")
        for m in models:
            name = m.get('name')
            print(f" - '{name}'")
            
            # Probar este modelo
            url_gen = "http://localhost:11434/api/generate"
            payload = {"model": name, "prompt": "Hi", "stream": False}
            try:
                res_gen = requests.post(url_gen, json=payload, timeout=5)
                print(f"   Prueba '{name}': {res_gen.status_code}")
                if res_gen.status_code != 200:
                    print(f"   Error: {res_gen.text}")
            except Exception as e_gen:
                print(f"   Excepción prueba '{name}': {e_gen}")
                
    except Exception as e:
        print(f"Error general: {e}")

if __name__ == "__main__":
    diagnostic()
