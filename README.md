# Resumidor de Expedientes - Yanahuara DB

Este proyecto automatiza la generación de resúmenes para la columna `ane_htm` de la tabla `tramite.anexo` en la base de datos `yanahuara_db`. Utiliza inteligencia artificial (Llama 3.1) a través de Ollama para crear síntesis concisas de los documentos.

## Estructura del Proyecto

El sistema es modular para facilitar su mantenimiento:

- `summarizer.py`: Punto de entrada principal para ejecutar el procesamiento.
- `src/db/operations.py`: Gestiona la conexión y operaciones con PostgreSQL, incluyendo la creación automática de columnas.
- `src/ai/inference.py`: Gestiona la comunicación con la API de Ollama/Llama 3.1.
- `src/processor/text_cleaner.py`: Limpia y prepara el texto (HTML) para la IA.
- `requirements.txt`: Lista de dependencias de Python.
- `.env.example`: Plantilla para la configuración de variables de entorno.

## Características Principales

- **Portabilidad**: El script busca el archivo `.env` automáticamente en su propia carpeta, facilitando su uso en distintos equipos.
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
2. Crea una copia de `.env.example` y llámala `.env`:
   ```bash
   copy .env.example .env
   ```
3. Edita el archivo `.env` con tus credenciales de base de datos y la URL de Ollama.
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Cómo usarlo

Para procesar los registros pendientes de resumen, simplemente ejecuta:

```powershell
python summarizer.py
```

El script buscará el archivo `.env` en la misma carpeta donde se encuentra.

## Registro de Errores

Si ocurre algún problema durante la inferencia de la IA, los detalles se guardarán en `error_log.txt`.