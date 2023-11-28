import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from lemmymodbot.data import base
from lemmymodbot.data.base import PostPhashHistory, Base, session_scope
from lemmymodbot.data.dao.post_phash_history_dao import PostPhashHistoryDao
from lemmymodbot.data.models.phash_models import PostInfo


class TestPhashDao(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        base.session_maker = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

        with session_scope() as session:
            session.add(PostPhashHistory(
                community_id=1,
                url='https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png',
                phash='c0803f7fffff0404'
            ))
            session.add(PostPhashHistory(
                community_id=1,
                url='https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png',
                phash='c0803f7fffff0404'
            ))
            session.add(PostPhashHistory(
                community_id=2,
                url='https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png',
                phash='c0803f7fffff0404'
            ))
            session.add(PostPhashHistory(
                community_id=2,
                url='https://picsum.photos/200/300',
                phash='f8f8f0d0c0c0c080'
            ))

            session.commit()

        self.dao = PostPhashHistoryDao()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        pass

    def test_get_posts_by_phash(self):
        # check that all posts with the requested phash are returned
        result = self.dao.get_posts_by_phash('c0803f7fffff0404')
        expected = [PostInfo(post_id=1, phash='c0803f7fffff0404'), PostInfo(post_id=2, phash='c0803f7fffff0404'),
                    PostInfo(post_id=3, phash='c0803f7fffff0404')]

        self.assertListEqual(result, expected)

    def test_is_duplicate_image(self):
        # check for image that does exist in community
        result = self.dao.is_duplicate_image('c0803f7fffff0404', 1)
        self.assertTrue(result)

        result = self.dao.is_duplicate_image('f8f8f0d0c0c0c080', 2)
        self.assertTrue(result)

        # check for image that does exist but in a different community
        result = self.dao.is_duplicate_image('f8f8f0d0c0c0c080', 1)
        self.assertFalse(result)

        # check for image that dosent exist in any community
        result = self.dao.is_duplicate_image('abcdefghijklmnop', 1)
        self.assertFalse(result)

    def test_add_post(self):

        # add an image with the add post function and check if it was added by checking if a duplicate exists
        self.dao.add_post(3, 'test_url.com', '1234567890123456')

        self.assertTrue(self.dao.is_duplicate_image('1234567890123456', 3))

