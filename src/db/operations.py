import os
import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'yanahuara_db'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASS', '1234'),
        port=os.getenv('DB_PORT', '5432')
    )

def init_db():
    """Crea la columna resumen si no existe."""
    table = os.getenv('DB_TABLE', 'tramite.anexo')
    summary_col = os.getenv('DB_SUMMARY_COL', 'resumen')
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"ALTER TABLE {table} ADD COLUMN IF NOT EXISTS {summary_col} TEXT;")
    conn.commit()
    cur.close()
    conn.close()
    print(f"[INFO] Verificación de esquema en {table} completada.")

def get_pending_records(limit=100):
    table = os.getenv('DB_TABLE', 'tramite.anexo')
    id_col = os.getenv('DB_ID_COL', 'ane_ide')
    text_col = os.getenv('DB_TEXT_COL', 'ane_htm')
    summary_col = os.getenv('DB_SUMMARY_COL', 'resumen')
    
    conn = get_db_connection()
    cur = conn.cursor()
    # Query simplificada para generalización
    query = f"""
        SELECT {id_col}, {text_col} 
        FROM {table}
        WHERE {text_col} IS NOT NULL AND {text_col} != ''
        AND ({summary_col} IS NULL OR {summary_col} = '')
        LIMIT %s;
    """
    cur.execute(query, (limit,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def update_summary(record_id, summary):
    table = os.getenv('DB_TABLE', 'tramite.anexo')
    id_col = os.getenv('DB_ID_COL', 'ane_ide')
    summary_col = os.getenv('DB_SUMMARY_COL', 'resumen')
    
    conn = get_db_connection()
    cur = conn.cursor()
    update_query = f"UPDATE {table} SET {summary_col} = %s WHERE {id_col} = %s"
    cur.execute(update_query, (summary, record_id))
    conn.commit()
    cur.close()
    conn.close()
    return True
