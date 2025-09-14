import uuid
from abc import ABC
from typing import TypeVar, Type, Generic
from sqlalchemy import Select, Update, Delete
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from .models import Notes, BaseModel

BASE_MODEL_TYPE = TypeVar("BASE_MODEL_TYPE", bound=BaseModel)


class Irepo(ABC, Generic[BASE_MODEL_TYPE]):

    @property
    def _model(self) -> Type[BASE_MODEL_TYPE]:
        raise NotImplementedError

    async def get(self, uuididf: uuid.UUID) -> BASE_MODEL_TYPE:
        raise NotImplementedError

    async def update(self, old: Notes, data: dict) -> BASE_MODEL_TYPE:
        raise NotImplementedError

    async def delete(self, uuididf: uuid.UUID) -> uuid.UUID:
        raise NotImplementedError

    async def create(self, data: dict) -> BASE_MODEL_TYPE:
        raise NotImplementedError

    async def get_list(self, user_id: uuid.UUID) -> list[BASE_MODEL_TYPE]:
        raise NotImplementedError


class NotesRepository(Irepo[Notes]):

    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory = session_factory

    @property
    def _model(self) -> Notes:
        return Notes

    async def get(self, uuididf: uuid.UUID) -> Notes:
        async with self.session_factory() as session:
            stmt = Select(self._model).where(self._model.uuididf == uuididf)
            note = (await session.execute(stmt)).scalar_one_or_none()
            return note

    async def create(self, data: dict) -> Notes:
        async with self.session_factory() as session:
            instance = self._model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def update(self, old: Notes, data: dict) -> Notes:
        async with self.session_factory() as session:
            stmt = (
                Update(self._model)
                .where(self._model.uuididf == old.uuididf)
                .values(**data)
                .returning(self._model)
            )
            instance = (await session.execute(stmt)).scalar_one_or_none()
            return instance

    async def delete(self, uuididf: uuid.UUID) -> uuid.UUID:
        async with self.session_factory() as session:
            stmt = (
                Delete(self._model)
                .where(self._model.uuididf == uuididf)
                .returning(self._model.uuididf)
            )
            deleted_uuididf = (await session.execute(stmt)).scalar()
            return deleted_uuididf

    async def get_list(self, user_id: uuid.UUID) -> list[Notes]:
        async with self.session_factory() as session:
            stmt = Select(self._model).where(self._model.user_id == user_id)
            list_of_notes = (await session.execute(stmt)).scalars()
            return list_of_notes
