from pydantic_settings import BaseSettings

class Settings(BaseSettings):
	replica: int = 0
