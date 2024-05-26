from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str

    JWT_SECRET_KEY: str

    # Database
    SQLALCHEMY_DATABASE_URI: str
    DATABASE_NAME: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
