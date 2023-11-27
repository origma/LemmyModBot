from sqlalchemy import func
from sqlalchemy.orm import Session

from lemmymodbot.data.base import Community, UserCommunityStatistics


class CommunityPersistence:

    def get_community_page_by_name(self, community_name: str, session: Session) -> Community:
        return session.query(Community.query.filter(Community.community_name == community_name)).one()

    def get_community_page_by_id(self, community_id: int, session: Session) -> Community:
        return session.query(Community.query.filter(Community.community_id == community_id)).one_or_none()

    def get_community_statistics(self, community_id: int, session: Session):

        query_result = session.query(UserCommunityStatistics.query.filter(UserCommunityStatistics.community_id == community_id))
        return session.query(query_result, func.count(UserCommunityStatistics.community_id)).group_by(UserCommunityStatistics.community_id).all()
