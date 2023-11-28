from sqlalchemy.orm import Session

from lemmymodbot.data.base import Community, session_scope


class CommunityDao:

    def get_community_page_by_name(self, community_name: str) -> Community | None:
        with session_scope(False) as session:
            return session.query(Community).filter_by(community_name=community_name).one_or_none()

    def get_community_page_by_id(self, community_id: int) -> Community | None:
        with session_scope(False) as session:
            return session.query(Community).filter_by(community_id=community_id).one_or_none()
