from lemmymodbot.data.dao.post_phash_history_dao import PostPhashHistoryDao
from lemmymodbot.data.models.phash_models import PostInfo


class PhashPersistence:
    post_phash_history_dao: PostPhashHistoryDao

    def __init__(self, post_phash_history_dao=PostPhashHistoryDao()):
        self.post_phash_history_dao = post_phash_history_dao

    def get_posts_by_phash(self, phash: str) -> [PostInfo]:
        return self.post_phash_history_dao.get_posts_by_phash(phash)

    def is_duplicate_image(self, phash: str, community_id: int) -> bool:
        return self.post_phash_history_dao.is_duplicate_image(phash, community_id)

    def add_post(self, community_id: int, url: str, phash: str):
        self.post_phash_history_dao.add_post(community_id, url, phash)
