import os
import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database='yanahuara_db',
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASS', '1234'),
        port=os.getenv('DB_PORT', '5432')
    )

def init_db():
    """Crea la columna resumen si no existe."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("ALTER TABLE tramite.anexo ADD COLUMN IF NOT EXISTS resumen TEXT;")
    conn.commit()
    cur.close()
    conn.close()
    print("[INFO] Verificación de esquema de base de datos completada.")

def get_pending_records(limit=100):
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
        SELECT a.ane_ide, a.ane_htm 
        FROM tramite.anexo a
        INNER JOIN tramite.expediente e ON e.exp_ide = a.exp_ide
        WHERE a.ane_htm IS NOT NULL AND a.ane_htm != ''
        AND (a.resumen IS NULL OR a.resumen = '')
        LIMIT %s;
    """
    cur.execute(query, (limit,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def update_summary(ane_ide, summary):
    conn = get_db_connection()
    cur = conn.cursor()
    update_query = "UPDATE tramite.anexo SET resumen = %s WHERE ane_ide = %s"
    cur.execute(update_query, (summary, ane_ide))
    conn.commit()
    cur.close()
    conn.close()
    return True
