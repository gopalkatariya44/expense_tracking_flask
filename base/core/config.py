from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str  # = "DriveInspector"

    JWT_SECRET_KEY: str
    # Database
    SQLALCHEMY_DATABASE_URI: str  # = config("MONGO_CONNECTION_STRING", cast=str)
    DATABASE_NAME: str

    MODEL_PATH: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
