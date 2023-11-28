from sqlalchemy import func
from sqlalchemy.orm import Session

from lemmymodbot.data.base import User, Content, ContentType, UserCommunityStatistics, Report, Outcome


class UserStatistics:

    def get_user_posts(self, actor_id: str, session: Session) -> [Content]:
        return session.query(
            Content.query.filter(Content.actor_id == actor_id and Content.content_type == ContentType.POST))

    def get_user_comments(self, actor_id: str, session: Session) -> [Content]:
        return session.query(
            Content.query.filter(Content.actor_id == actor_id and Content.content_type == ContentType.COMMENT))

    def get_user_statistics(self, actor_id: str, session: Session):
        # return the number of reports, warnings, removals and bans across all communities
        query_result = session.query(UserCommunityStatistics.query.filter(UserCommunityStatistics.actor_id == actor_id))
        return (session.query(query_result, func.count(UserCommunityStatistics.actor_id))
                .group_by(UserCommunityStatistics.actor_id).all())

    def get_user_reports(self, actor_id: str, session: Session) -> [Report]:
        return session.query(Report.query.filter(Report.actor_id == actor_id))

    def add_user(self, actor_id: str, session: Session):
        session.add(User(actor_id=actor_id))

    def add_report(self, actor_id: str, content_id: int, reason: str, outcome: Outcome, session: Session):
        session.add(Report(
            actor_id=actor_id,
            content_id=content_id,
            reason=reason,
            outcome=outcome
        ))
