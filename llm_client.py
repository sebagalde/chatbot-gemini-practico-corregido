import time
from typing import Dict, List, Optional
import google.generativeai as genai
from config import settings
class GeminiClient:
    def __init__(self, api_key: str, model_name: str):
        if not api_key:
            raise ValueError("GEMINI_API_KEY no está configurada.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(
        self,
        system_prompt: str,
        history: List[Dict[str, str]],
        user_message: str,
        max_retries: int,
        timeout_seconds: int
        ) -> str:
        """
        Manejo de errores con reintentos y backoff exponencial simple.
        """
        attempt = 0
        last_error: Optional[Exception] = None
        # Preparamos el historial como una conversación del SDK
        # Usamos start_chat para mantener contexto interno del modelo.
        # Pasamos system_prompt como primer mensaje del "usuario" para orientar el rol.
        # (Gemini no tiene "system" estricto, pero este patrón funciona bien)
        convo = self.model.start_chat(history=[{"role": "user", "parts": system_prompt}] +
        [{"role": m["role"], "parts": m["content"]} for m in history])
        while attempt < max_retries:
            try:
                # timeouts no están expuestos directamente; se controla por red.
                response = convo.send_message(user_message)
                text = getattr(response, "text", "")
                if not text:
                    raise RuntimeError("Respuesta vacía del modelo.")
                return text
            except Exception as e:
                last_error = e
                sleep_s = 2 ** attempt # 1, 2, 4...
                time.sleep(sleep_s)
                attempt += 1
        raise RuntimeError(f"Fallo tras {max_retries} reintentos. Último error: {last_error}")
