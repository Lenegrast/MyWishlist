from dataclasses import dataclass
from environs import Env

#Мы определяем класс DatabaseConfig для хранения URL подключения к базе данных.
@dataclass
class DatabaseConfig:
    database_url: str

#Класс Config объединяет все настройки проекта, включая секретный ключ и флаг отладки.
@dataclass
class Config:
    db: DatabaseConfig
    secret_key: str
    debug: bool

#Функция load_config() читает переменные окружения и возвращает объект класса Config.
def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path) # Загружаем переменные окружения из файла .env

    return Config(
        db = DatabaseConfig(database_url = env("DATABASE_URL")),
                            secret_key = env("SECRET_KEY"),
                            debug = env.bool("DEBUG", default = False),
        )