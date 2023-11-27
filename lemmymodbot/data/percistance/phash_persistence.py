from sqlalchemy import select
from sqlalchemy.orm import Session

from lemmymodbot.data.base import Community, session_scope, PostPhashHistory
from lemmymodbot.data.models.phash_models import PostInfo


class PhashPersistence:

    def get_posts_by_phash(self, phash: str, session: Session) -> [PostInfo]:
        query_results = session.query(PostPhashHistory.query.filter(PostPhashHistory.phash == phash))

        return [PostInfo(q.post_id, q.phash) for q in query_results]

    def is_duplicate_image(self, phash: str, community_id: int, session: Session) -> bool:
        return session.query(PostPhashHistory.query.filter(
            PostPhashHistory.phash == phash and PostPhashHistory.community_id == community_id
        ).exists()).scalar()

    def add_post(self, community_id: int, url: str, phash: str, session: Session):
        session.add(PostPhashHistory(
            community_id=community_id,
            url=url,
            phash=phash
        ))
