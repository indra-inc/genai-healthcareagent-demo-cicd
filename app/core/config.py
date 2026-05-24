import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = "Healthcare Agent"
    API_VERSION = "v1"

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


settings = Settings()
