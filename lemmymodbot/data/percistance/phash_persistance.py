from sqlalchemy import select
from sqlalchemy.orm import Session

from lemmymodbot.data.base import Community, session_scope, PostPhashHistory


class PhashPersistence:

    def get_phash_history_by_post(self, post_id: int, session: Session):
        pass

    def get_posts_by_phash(self, phash: str, session: Session) -> [int]:
        pass

    def is_duplicate_image(self, phash: str, community_name) -> bool:
        pass

    def add_post(self, post_id: int, community_id: int, url: str, phash: str, session: Session):
        session.add(PostPhashHistory(
            community_id = community_id,
            url = url,
            phash = phash
        ))
        #check df


    def _get_page_entry(self, community_name: str, session: Session) -> Community:
        return (session.execute(select(Community).filter(Community.community_name == community_name))
                .scalar_one_or_none())

    def get_current_page(self, community_name: str) -> int:
        pass

    def set_current_page(self, community_name: str, page_number: int):
        pass