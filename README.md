## Objetivo del proyecto
Este proyecto implementa un chatbot de consola escrito en Python, utilizando una arquitectura modular. Su propósito principal es demostrar cómo organizar un asistente conversacional que:

- Utiliza un cliente del modelo de lenguaje de Google Gemini (`google-generativeai`) para procesar las entradas del usuario.  
- Mantiene memoria de la conversación para recordar turnos anteriores.
- Define y utiliza diferentes roles y prompts (Profesor, Traductor, Programador, Asistente) para personalizar la interacción del modelo.

---

## Instalación de dependencias

## 1. Clonar el repositorio:

```bash
git clone <url-del-repositorio>
cd <carpeta-donde-se-clono>

## 2. Crear y activar un entorno virtual

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

## 3. Instalar las dependencias

pip install -r requirements.txt

## 4. Configurar un archivo .env en la raíz del proyecto con las variables necesarias:

GEMINI_API_KEY=<tu_api_key>
MODEL=<nombre_del_modelo>
MAX_RETRIES=3
TIMEOUT_SECONDS=30
MAX_HISTORY=12
SYSTEM_NAME=Chatbot

## Ejecución

python main.py

Mientras el chatbot está corriendo, puedes usar estos comandos especiales:

Comando	Función
:rol <nombre>	Cambia el rol del chatbot (opciones: profesor, traductor, programador, asistente).
:reset	Limpia la memoria de la conversación, iniciando un nuevo diálogo.
:salir	Finaliza la ejecución del programa.
:help	Muestra la lista de comandos disponibles.
Estructura del proyecto

main.py → Interfaz de línea de comandos y flujo principal.

chat_service.py → Clase ChatService que integra memoria, cliente LLM y prompts.

llm_client.py → Cliente Gemini con manejo de reintentos y backoff.

memory.py → Manejo de historial de conversación.

roles.py → Definición de roles y prompts asociados.

prompts.py → Construcción de prompts y manejo del historial.

config.py → Configuración centralizada mediante variables de entorno.

requirements.txt → Dependencias del proyecto.