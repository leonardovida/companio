"""
SQL Alchemy models declaration.
https://docs.sqlalchemy.org/en/14/orm/declarative_styles.html#example-two-dataclasses-with-declarative-table
Dataclass style for powerful autocompletion support.

https://alembic.sqlalchemy.org/en/latest/tutorial.html
Note, it is used by alembic migrations logic, see `alembic/env.py`

Alembic shortcuts:
# create migration
alembic revision --autogenerate -m "migration_name"

# apply all migrations
alembic upgrade head
"""
import uuid

from sqlalchemy import Boolean, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_model"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    email: Mapped[str] = mapped_column(
        String(254), nullable=False, unique=True, index=True
    )
    hashed_password: Mapped[str] = mapped_column(String(128), nullable=False)


class List(Base):
    __tablename__ = "list_model"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    city: Mapped[str] = mapped_column(String(100), nullable=True)
    list: Mapped[str] = mapped_column(String(4000), nullable=True)
    email: Mapped[str] = mapped_column(
        String(254), nullable=True, unique=False, index=True
    )
    phone: Mapped[str] = mapped_column(String(100), nullable=True)
    service: Mapped[str] = mapped_column(String(100), nullable=True)


class Note(Base):
    __tablename__ = "note_model"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    text: Mapped[str] = mapped_column(String(10000), nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)
