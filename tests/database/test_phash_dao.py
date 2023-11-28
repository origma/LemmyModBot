import unittest
from unittest.mock import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from lemmymodbot.data.base import PostPhashHistory


class TestPhashDao(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = Session(self.engine)
        Base.metadata.create_all(self.engine)
        self.session.add(PostPhashHistory(
            community_id=1,
            url='https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png',
            phash='c0803f7fffff0404'
        ))
        self.session.add(PostPhashHistory(
            community_id=1,
            url='https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png',
            phash='c0803f7fffff0404'
        ))
        self.session.add(PostPhashHistory(
            community_id=2,
            url='https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png',
            phash='c0803f7fffff0404'
        ))
        self.session.add(PostPhashHistory(
            community_id=2,
            url='https://picsum.photos/200/300',
            phash='f8f8f0d0c0c0c080'
        ))

        self.session.commit()

    def tearDown(self):
        #Base.metadata.drop_all(self.engine)
        pass

    def test_get_posts_by_phash(self):
        pass

    def test_is_duplicate_image(self):
        pass

    def test_add_post(self):
        pass
