from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.pool import NullPool
from .config import AbstractDBConfig


def create_session_factory(
    db_config: AbstractDBConfig,
) -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(
        db_config.get_connection_string(),
        poolclass=NullPool,
        echo=True,
    )
    session_factory = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    return session_factory
