import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lemmymodbot.data import base
from lemmymodbot.data.base import Base, session_scope, Community
from lemmymodbot.data.dao.community_dao import CommunityDao


class TestPhashDao(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        base.session_maker = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

        with session_scope() as session:
            session.add(Community(
                community_id=12345,
                community_name="test_community",
                post_page=2,
                comment_page=8
            ))
            session.add(Community(
                community_id=54321,
                community_name="AnotherCommunity",
                post_page=1,
                comment_page=1
            ))

            session.commit()

        self.dao = CommunityDao()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        pass


    def test_retreval_of_existing_community_by_id(self):

        # test retrieval of existing communities by id
        result = self.dao.get_community_page_by_name("test_community")
        self.assertEqual(result.community_id, 12345)

        result = self.dao.get_community_page_by_name("AnotherCommunity")
        self.assertEqual(result.community_id, 54321)

    def test_retrieval_of_nonexistent_community_by_id(self):

        result = self.dao.get_community_page_by_name("non_existent_name")
        self.assertIsNone(result)



    def def_test_retrieval_of_existing_community_by_name(self):
        # test retrieval of existing communities by id
        result = self.dao.get_community_page_by_id(12345)
        self.assertEqual(result.community_name, "test_community")

        result = self.dao.get_community_page_by_id(54321)
        self.assertEqual(result.community_name, "AnotherCommunity")


    def def_test_retrieval_of_nonexistent_community_by_name(self):

        result = self.dao.get_community_page_by_id(6789)
        self.assertIsNone(result)
