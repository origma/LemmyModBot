from sqlalchemy.orm import Session

from lemmymodbot.data.base import Content


class ContentPersistence:

    def get_content(self, content_id: int, session: Session) -> Content:

        pass

        #return session.query(Content.query.filter())
