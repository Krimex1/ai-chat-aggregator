# config.py

import os

# --- APP CONFIG ---

PORT = 25625

SITE_NAME = "LocalVisionChat"

REFERER = "http://localhost:25625"

# --- API CONFIG ---

API_KEY = os.getenv("OPENROUTER_API_KEY", "your-api-key-here")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# --- MODELS ---

FALLBACK_MODELS = [
    "mistralai/devstral-2512:free",
    "amazon/nova-2-lite-v1:free",
    "google/gemini-2.0-flash-exp:free",
    "nvidia/nemotron-nano-12b-v2-vl:free",
    "deepseek/deepseek-chat-v3.1",
]

CODING_MODELS = {
    "kwaipilot/kat-coder-pro:free": "KAT-Coder-Pro V1",
}

# Дефолтная модель для кода (используется в Pydantic и аргументах функций)
DEFAULT_CODING_MODEL = "kwaipilot/kat-coder-pro:free"
