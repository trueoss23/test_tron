from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..config import get_settings

cfg = get_settings()
DATABASE_URL = f"postgresql+psycopg2://{cfg.db_user}:{cfg.db_pass}@{cfg.db_host}:{cfg.db_port}/{cfg.db_name}"

Base = declarative_base()


class TronRequest(Base):
    __tablename__ = 'tron'

    id = Column(Integer, primary_key=True)
    address = Column(String(34), nullable=False)
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
