from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_CONNECTION_STRING: str
    BOT_TOKEN: str
    ADMIN_ID: int
    CRYPTOBOT_TOKEN: str
    LOLZ_TOKEN: str
    AAIO_TOKEN: str

    class Config:
        env_file = ".env"

settings = Settings()
