from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="settings.env", env_file_encoding="utf-8"
    )
    groq_api_key: str


config = Settings()
# print(config.model_dump())
