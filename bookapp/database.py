import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

try:
    from bookapp.config import DATABASE_URL
except ModuleNotFoundError:
    DATABASE_URL = "sqlite+aiosqlite:///./predictions.db"

engine = create_async_engine(DATABASE_URL)

async_session = _orm.sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = _declarative.declarative_base()

