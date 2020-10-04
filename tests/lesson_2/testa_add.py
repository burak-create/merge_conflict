import unittest
from lesson_2 import utils


class HappyPathTestCase(unittest.TestCase):

    def test_ones(self):
        self.assertEqual(utils.add(1, 1), 2)

    def test_device(self):
        self.assertEqual(utils.decide_branch(True), True)


if __name__ == '__main__':
    unittest.main()
