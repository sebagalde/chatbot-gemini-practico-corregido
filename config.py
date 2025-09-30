from dataclasses import dataclass
import os
from dotenv import load_dotenv
load_dotenv()
@dataclass(frozen=True)
class Settings:
    api_key: str = os.getenv("GEMINI_API_KEY", "")
    model: str = os.getenv("MODEL", "")
    max_retries: int = int(os.getenv("MAX_RETRIES", "3")) # Reintentos ante fallos
    timeout_seconds: int = int(os.getenv("TIMEOUT_SECONDS", "30"))
    max_history_messages: int = int(os.getenv("MAX_HISTORY", "12")) # Máximo de mensajesen memoria de conversación
    system_name: str = os.getenv("SYSTEM_NAME", "Chatbot")
settings = Settings()