from lemmymodbot.data import session_scope
from lemmymodbot.data.base import PostPhashHistory
from lemmymodbot.data.models.phash_models import PostInfo


class PostPhashHistoryDao:
    def get_posts_by_phash(self, phash: str) -> [PostInfo]:
        with session_scope() as session:
            query_results = session.query(PostPhashHistory).filter_by(phash=phash)

            return [PostInfo(q.post_id, q.phash) for q in query_results]

    def is_duplicate_image(self, phash: str, community_id: int) -> bool:
        with session_scope() as session:

            return bool(
                session.query(PostPhashHistory).filter_by(phash=phash).filter_by(community_id=community_id).first())

    def add_post(self, community_id: int, url: str, phash: str):
        with session_scope() as session:
            session.add(PostPhashHistory(
                community_id=community_id,
                url=url,
                phash=phash
            ))
