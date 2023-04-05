from functools import lru_cache

from config import Settings
from sqlmodel import Session, create_engine


@lru_cache()
def get_settings():
    return Settings()


api_engine = create_engine(get_settings().DATABASE_URI, echo=True)


async def get_session():
    with Session(api_engine) as session:
        yield session
