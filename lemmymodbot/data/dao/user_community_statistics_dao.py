from sqlalchemy import func
from sqlalchemy.orm import Session

from lemmymodbot.data import session_scope
from lemmymodbot.data.base import UserCommunityStatistics


class UserCommunityStatisticsDao:

    def get_community_statistics(self, community_id: int):

        with session_scope() as session:
            query_result = session.query(
                UserCommunityStatistics.query.filter(UserCommunityStatistics.community_id == community_id))
            return session.query(query_result, func.count(UserCommunityStatistics.community_id)).group_by(
                UserCommunityStatistics.community_id).all()