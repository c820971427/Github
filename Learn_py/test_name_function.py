import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """ 测试 name_function.py """

    def test_first_last_name(self):
        formatted_name = get_formatted_name('Chen', 'Shilei')
        self.assertEqual(formatted_name, 'Chen  Shilei')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('chen', 'lei', 'shi')
        self.assertEqual(formatted_name, 'Chen Shi Lei')

    def test_fist_middle_name(self):
        formatted_name = get_formatted_name('wang', 'xia', 'jin')
        self.assertEqual(formatted_name, 'Wang Jin Xia')


if __name__ == '__main__':
    unittest.main()
