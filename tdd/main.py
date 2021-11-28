import unittest
import get_roots


class TestGetRoots(unittest.TestCase):
    # x^4+2x^2+3 = 0
    def test_no_roots(self):
        self.assertEqual(get_roots.get_roots(1, 2, 3), [])

    def test_four_roots(self):
        expected_len = 4
        expected_value = [-1, 1, 0.5, -0.5]

        cur_value = get_roots.get_roots(4, -5, 1)
        self.assertEqual(len(cur_value), expected_len)
        self.assertEqual(expected_value[0] in cur_value, True)
        self.assertEqual(expected_value[1] in cur_value, True)
        self.assertEqual(expected_value[2] in cur_value, True)
        self.assertEqual(expected_value[3] in cur_value, True)


if __name__ == "__main__":
    unittest.main()
