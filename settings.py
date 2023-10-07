from pydantic_settings import BaseSettings

class Settings(BaseSettings):
	replica: int = 0
	database_url: str

	class Config:
		env_file = '.env'
		env_file_encoding = 'utf-8'
