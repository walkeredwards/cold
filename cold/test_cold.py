"""test cold.py
"""

import unittest
from cold import answer


class TestCold(unittest.TestCase):
    def test_answer(self) -> None:
        data = '-3 -454 0 454 -565656 -45445'
        ans = answer(data)
        expected = 4
        self.assertEqual(ans, expected)

    def test_answer1(self) -> None:
        self.assertEqual(answer('23 32 6 566 7757'), 0)
