# Resumidor de Expedientes - Yanahuara DB

Este proyecto automatiza la generación de resúmenes para la columna `ane_htm` de la tabla `tramite.anexo` en la base de datos `yanahuara_db`. Utiliza inteligencia artificial (Llama 3.1) a través de Ollama para crear síntesis concisas de los documentos.

## Estructura del Proyecto

El sistema es modular para facilitar su mantenimiento:

- `summarizer.py`: Punto de entrada principal para ejecutar el procesamiento.
- `src/db/operations.py`: Gestiona la conexión y operaciones con PostgreSQL, incluyendo la creación automática de columnas.
- `src/ai/inference.py`: Gestiona la comunicación con la API de Ollama/Llama 3.1.
- `src/processor/text_cleaner.py`: Limpia y prepara el texto (HTML) para la IA.
- `requirements.txt`: Lista de dependencias de Python.
- `.env`: Archivo de configuración (ubicado en `RESUMIDOR/`).

## Características Principales

- **Modulariad**: Código separado por responsabilidades (DB, AI, Procesamiento).
- **Inicialización Automática**: El script crea la columna `resumen` automáticamente si no existe en la tabla `tramite.anexo`.
- **Limpieza de HTML**: Extrae el texto plano de los campos HTML antes de enviarlos a la IA.
- **Configurable**: Parámetros de conexión y modelo gestionados por variables de entorno.

## Requisitos

1. **PostgreSQL**: Tener acceso a la base de datos `yanahuara_db`.
2. **Ollama**: Instalado y con el modelo `llama3.1` descargado (`ollama pull llama3.1`).
3. **Python 3.x**: Instalación de dependencias.

## Instalación

1. Clona el repositorio.
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Configuración

Asegúrate de que el archivo `.env` en `d:\proyecto de investigacion\RESUMIDOR\.env` tenga los valores correctos:

```text
DB_HOST=localhost
DB_NAME=yanahuara_db
DB_USER=postgres
DB_PASS=1234
DB_PORT=5432
AI_MODEL=llama3.1:latest
OLLAMA_URL=http://localhost:11434/api/generate
```

## Cómo usarlo

Para procesar los registros pendientes de resumen, simplemente ejecuta:

```powershell
python summarizer.py
```

El script:
1. Verificará que el esquema de la base de datos sea correcto (creará la columna `resumen` si falta).
2. Buscará registros que no tengan resumen.
3. Generará y guardará el resumen para cada uno.

## Registro de Errores

Si ocurre algún problema durante la inferencia de la IA, los detalles se guardarán en `error_log.txt`.