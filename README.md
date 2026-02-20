# Resumidor Universal de Tablas - PostgreSQL & Llama 3.1

Este proyecto es una herramienta flexible para generar resúmenes automáticos de cualquier tabla en una base de datos PostgreSQL utilizando el modelo Llama 3.1 (vía Ollama).

## Características

- **Totalmente Configurable**: No necesitas modificar el código. Todo se controla desde el archivo `.env`.
- **Generalizado**: Funciona con cualquier tabla que tenga un identificador y una columna de texto.
- **Limpieza Automática**: Remueve etiquetas HTML antes de procesar el texto.
- **Idempotente**: No procesa registros que ya tienen un resumen.
- **Seguro**: Crea automáticamente la columna de resumen si no existe.

## Estructura del Proyecto

- `summarizer.py`: Punto de entrada modular.
- `src/db/operations.py`: Lógica genérica de base de datos.
- `src/ai/inference.py`: Comunicación con Ollama.
- `src/processor/text_cleaner.py`: Limpieza de texto.

## Configuración (.env)

El script construye su propia consulta basada en estas variables. Aquí te explico cómo se traduce tu necesidad a la configuración:

Si tu consulta original era:
`SELECT id_unico, contenido_html FROM mi_esquema.mi_tabla;`

Tu configuración en el `.env` debe ser:

```text
# Conexión
DB_HOST=localhost
DB_NAME=tu_base_de_datos
DB_USER=postgres
DB_PASS=tu_password
DB_PORT=5432

# Configuración Genérica de la Tabla
DB_TABLE=mi_esquema.mi_tabla      # Nombre de la tabla (con esquema si aplica)
DB_ID_COL=id_unico                 # La columna que sirve de ID para el registro
DB_TEXT_COL=contenido_html         # La columna que tiene el texto/HTML a resumir
DB_SUMMARY_COL=resumen            # Nombre de la columna donde se guardará el resumen
```

## Requisitos

1. **PostgreSQL**: Tener acceso a la base de datos.
2. **Ollama**: Instalado y con el modelo `llama3.1` descargado (`ollama pull llama3.1`).
3. **Python 3.x**: Instalación de dependencias.

## Instalación y Uso

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Configura tu `.env` (usa `.env.example` como guía).
3. Ejecuta el resumidor:
   ```bash
   python summarizer.py
   ```

## Funcionamiento Interno
El script realiza los siguientes pasos automáticamente:
1. Verifica si existe la columna de resumen; si no, la crea.
2. Busca registros que tengan texto pero cuyo campo de resumen esté vacío (`NULL`).
3. Limpia el HTML del texto extraído.
4. Genera el resumen con Llama 3.1 y actualiza la fila correspondiente en la DB.

## Cómo usarlo

Para procesar los registros pendientes de resumen, simplemente ejecuta:

```powershell
python summarizer.py
```

El script buscará el archivo `.env` en la misma carpeta donde se encuentra.

## Ver Resultados

Para verificar los resúmenes generados en tu base de datos, puedes ejecutar la siguiente consulta SQL:

```sql
SELECT 
    DB_ID_COL, 
    DB_TEXT_COL, 
    DB_SUMMARY_COL 
FROM DB_TABLE 
WHERE DB_SUMMARY_COL IS NOT NULL;
```

*(Reemplaza los nombres de las columnas y la tabla por los que configuraste en tu `.env`)*.

## Registro de Errores
Cualquier fallo durante el procesamiento se registrará en `error_log.txt`.