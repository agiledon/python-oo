import unittest

from automation.common import Common


class TestCommon(unittest.TestCase):
    def test_should_join_lines_if_not_contain_spec_word(self):
        lines = ['Python is a dynamic language',
                 'Python support functional programming',
                 'I love Python']
        result = Common._join_lines_if_not_contain(lines, 'language', '|')
        self.assertEqual('Python support functional programming|I love Python', result)
