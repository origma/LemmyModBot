from lemmymodbot.data.base import Community
from lemmymodbot.data.dao.community_dao import CommunityDao
from lemmymodbot.data.dao.user_community_statistics_dao import UserCommunityStatisticsDao


class CommunityPersistence:

    community_dao: CommunityDao
    user_community_statistics_dao = UserCommunityStatisticsDao

    def __init__(self, community_dao=CommunityDao(), user_community_statistics_dao=UserCommunityStatisticsDao()):
        self.community_dao = community_dao
        self.user_community_statistics_dao = user_community_statistics_dao

    def get_community_page_by_name(self, community_name: str) -> Community:
        return self.community_dao.get_community_page_by_name(community_name)

    def get_community_page_by_id(self, community_id: int) -> Community:
        return self.community_dao.get_community_page_by_id(community_id)

    def get_community_statistics(self, community_id: int):
        return self.user_community_statistics_dao.get_community_statistics(community_id)
