# config.py
import os

# --- APP CONFIG ---
PORT = 25625
SITE_NAME = "LocalVisionChat"
REFERER = "http://localhost:25625"

# --- API CONFIG ---
API_KEY = "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"
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
