import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ЗАМЕНИТЕ ЭТИ ДАННЫЕ НА ТЕ, ЧТО МЫ ТОЛЬКО ЧТО НАШЛИ!
DB_USER = "postgres"
DB_PASSWORD = "12345"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

# Строка подключения
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(DATABASE_URL)
    
    from sqlalchemy.orm import declarative_base
    from sqlalchemy import Column, Integer, String
    
    Base = declarative_base()
    
    # --- ВОТ ТУТ МЫ ОПИСЫВАЕМ ТАБЛИЦУ ---
    class Student(Base):
        __tablename__ = 'students'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        age = Column(Integer)
        email = Column(String)
    # -------------------------------------

    Base.metadata.create_all(engine) 
    
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    
