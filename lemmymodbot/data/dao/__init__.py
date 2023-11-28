import unittest
from unittest.mock import Mock

from post_phash_history_dao import *

class TestPostPaginator(unittest.TestCase):
    def setUp(self):
        self.mock_lemmy = Mock()
        self.mock_handle = Mock()


    def test_task_called_correct_number_of_times(self):
        pass