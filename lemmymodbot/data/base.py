import enum
from contextlib import contextmanager

from sqlalchemy import Column, create_engine, Engine, ForeignKey, Enum
from sqlalchemy.dialects.mysql import INTEGER, TEXT, VARCHAR, TIMESTAMP, BOOLEAN
from sqlalchemy.orm import sessionmaker, Session, mapped_column, declarative_base

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


class Community(Base):

    __tablename__ = 'community'

    community_id = mapped_column(INTEGER, primary_key=True)

    community_name = Column(VARCHAR(30), nullable=False)
    post_page = Column(INTEGER)
    comment_page = Column(INTEGER)


class UserCommunityStatistics(Base):
    __tablename__ = 'user_community_statistics'

    statistics_id = Column(INTEGER, primary_key=True)
    actor_id = mapped_column(ForeignKey("user.actor_id"))
    community_id = mapped_column(ForeignKey("community.community_id"))

    report_count = Column(INTEGER)
    warned_count = Column(INTEGER)
    removed_count = Column(INTEGER)
    ban_count = Column(INTEGER)
    banned_until = Column(TIMESTAMP, nullable=True)


class User(Base):
    __tablename__ = 'user'

    actor_id = mapped_column(VARCHAR, primary_key=True)


class Outcome(enum.Enum):
    REMOVED = 1
    DISMISSED = 2


class Report(Base):
    __tablename__ = 'report'

    report_id = Column(INTEGER, primary_key=True)
    actor_id = mapped_column(ForeignKey("user.actor_id"))
    content_id = mapped_column(ForeignKey("content.content_id"))

    reason = Column(TEXT)
    outcome = Column(Enum(Outcome))


class ContentType(enum.Enum):
    POST = 1
    COMMENT = 2


class Content(Base):
    __tablename__ = 'content'

    content_id = mapped_column(INTEGER, primary_key=True)
    actor_id = mapped_column(ForeignKey("user.actor_id"))
    community_id = mapped_column(ForeignKey("community.community_id"))
    # the immediate parent of the content e.g. the comment that a comment is replying to
    parent_content_id = mapped_column(ForeignKey("content.content_id"), nullable=True)
    # the highest level parent of the content (ie the post)
    root_content_id = Column(INTEGER, nullable=True)

    content_type = Column(Enum(Outcome))
    # the actual id of the post or comment
    lemmy_content_id = Column(INTEGER)
    should_rescan = Column(BOOLEAN)


class ContentFieldType(enum.Enum):
    COMMENT_CONTENT = 1
    POST_CONTENT = 2
    POST_TITLE = 3
    POST_URL = 4


class ContentField(Base):
    __tablename__ = 'content_field'

    content_field_id = mapped_column(INTEGER, primary_key=True)
    content_id = mapped_column(ForeignKey("content.content_id"))

    content_field_type = Column(Enum(ContentFieldType))


class ContentFieldHistory(Base):
    __tablename__ = "content_field_history"

    content_field_history_id = mapped_column(INTEGER, primary_key=True)
    content_field_id = mapped_column(ForeignKey("content_field.content_field_id"))

    content = Column(TEXT)
    timestamp = Column(TIMESTAMP)
    scan_timestamp = Column(TIMESTAMP)


class ContentResult(Base):
    __tablename__ = 'content_result'

    content_result_id = mapped_column(INTEGER, primary_key=True)
    content_field_history_id = mapped_column(ForeignKey("content_field_history.content_field_history_id"))
    content_id = mapped_column(ForeignKey("content.content_id"))

    processor = Column(VARCHAR(30))
    tags = Column(TEXT)
    current = Column(BOOLEAN)


class ContentMetadata(Base):
    __tablename__ = 'content_metadata'

    content_metadata_id = Column(INTEGER, primary_key=True)
    content_field_history_id = mapped_column(ForeignKey("content_field_history.content_field_history_id"))
    content_id = mapped_column(ForeignKey("content.content_id"))

    key = Column(TEXT)
    value = Column(TEXT)
    current = Column(BOOLEAN)


class PostPhashHistory(Base):
    __tablename__ = 'post_phash_history'

    post_id = Column(INTEGER, primary_key=True, autoincrement=True)

    community_id = Column(INTEGER)
    url = Column(TEXT)
    phash = Column(VARCHAR(16))

