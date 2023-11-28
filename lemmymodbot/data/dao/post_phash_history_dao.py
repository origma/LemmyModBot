from lemmymodbot.data import session_scope
from lemmymodbot.data.base import PostPhashHistory
from lemmymodbot.data.models.phash_models import PostInfo


class PostPhashHistoryDao:
    def get_posts_by_phash(self, phash: str) -> [PostInfo]:
        with session_scope() as session:
            query_results = session.query(PostPhashHistory.query.filter(PostPhashHistory.phash == phash))

            return [PostInfo(q.post_id, q.phash) for q in query_results]

    def is_duplicate_image(self, phash: str, community_id: int) -> bool:
        with session_scope() as session:
            return session.query(PostPhashHistory.query.filter(
                PostPhashHistory.phash == phash and PostPhashHistory.community_id == community_id
            ).exists()).scalar()

    def add_post(self, community_id: int, url: str, phash: str):
        with session_scope() as session:
            session.add(PostPhashHistory(
                community_id=community_id,
                url=url,
                phash=phash
            ))