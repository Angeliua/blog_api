from dataclasses import dataclass

@dataclass
class User:
    """Обычный пользователь"""
    id: str

@dataclass
class Admin(User):
    """Пользователь, наделенный правами администратора"""
    id: str
    password: str

@dataclass
class Article:
    """Сущность статьи"""
    id: str
    title: str
    content: str