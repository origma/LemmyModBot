import enum
from contextlib import contextmanager

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, Engine, ForeignKey, Enum
from sqlalchemy.dialects.mysql import INTEGER, TEXT, VARCHAR, TIMESTAMP, BOOLEAN
from sqlalchemy.orm import sessionmaker, Session, mapped_column

Base = declarative_base()
metadata = Base.metadata

engine: Engine = create_engine('sqlite:///data/database.db', echo=False)
session_maker = sessionmaker(bind=engine)


@contextmanager
def session_scope() -> Session:
    """Provide a transactional scope around a series of operations."""
    session = session_maker()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class CurrentPage(Base):
    __tablename__ = 'current_page'

    community_name = Column(VARCHAR(30), primary_key=True)
    post_page = Column(INTEGER)
    comment_page = Column(INTEGER)
