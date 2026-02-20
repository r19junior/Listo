import os
from dotenv import load_dotenv
from src.db.operations import get_pending_records, update_summary, init_db
from src.processor.text_cleaner import clean_html
from src.ai.inference import generate_summary

# Cargar configuración desde el .env del proyecto RESUMIDOR
dotenv_path = r"d:\proyecto de investigacion\RESUMIDOR\.env"
load_dotenv(dotenv_path)

def main():
    try:
        init_db() # Crea la columna si no existe
        rows = get_pending_records(limit=10) # Procesar de a 10 para control
        
        if not rows:
            print("[INFO] No hay registros pendientes de resumen.")
            return

        print(f"[INFO] Procesando {len(rows)} registros...")
        
        for ane_ide, ane_htm in rows:
            text = clean_html(ane_htm)
            summary = generate_summary(text, ane_ide)
            
            if summary:
                update_summary(ane_ide, summary)
                print(f"[OK] ID {ane_ide}: Resumen generado exitosamente.")
            else:
                print(f"[WARN] ID {ane_ide}: No se pudo generar resumen.")

        print("[INFO] Proceso finalizado.")

    except Exception as e:
        print(f"[CRITICAL ERROR] {e}")

if __name__ == "__main__":
    main()
