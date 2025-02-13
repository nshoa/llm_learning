import os

from dotenv import load_dotenv

load_dotenv()

# APP
API_PORT = int(os.getenv("API_PORT"))
CORS_ALLOWED_ORIGINS: list = [
    *(filter(lambda x: len(x) > 0, os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")))
]

# LLM
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
