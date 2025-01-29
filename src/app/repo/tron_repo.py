from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Параметры подключения
DATABASE_URL = "postgresql+psycopg2://ваш_пользователь:ваш_пароль@localhost:5432/ваша_база_данных"

# Создание базы
Base = declarative_base()


class TronRequest(Base):
    __tablename__ = 'tron'

    id = Column(Integer, primary_key=True)
    address = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

# Создание подключения
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # Создание таблицы

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

print("Таблица 'users' успешно создана с использованием SQLAlchemy")

# Закрытие сессии
session.close()
!!! нужно добавить сохранение, получение +  тесты