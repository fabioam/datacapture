import unittest
from main import DataCapture

NUMBER_LIST = [3, 9, 3, 4, 6]

LESS_PROVIDED_VS_EXPECTED_VALUES = (
    (3, 0),
    (4, 2),
    (6, 3),
    (9, 4),
)

BETWEEN_VS_EXPECTED_VALUES = (
    ([4, 6], 2),
    ([3, 6], 4),
)

GREATER_PROVIDED_VS_EXPECTED_VALUES = (
    (3, 3),
    (4, 2),
    (6, 1),
    (9, 0),
)

INVALID_KEY_VALUES = [9999, 7364, 81272]


class TestDataCaptureMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.capture = DataCapture()
        [cls.capture.add(i) for i in NUMBER_LIST]
        cls.capture.build_stats()

    def test_less(self):
        [self.assertEqual(self.capture.less(i[0]), i[1]) for i in LESS_PROVIDED_VS_EXPECTED_VALUES]

    def test_between(self):
        for i in BETWEEN_VS_EXPECTED_VALUES:
            self.assertEqual(self.capture.between(i[0][0], i[0][1]), i[1])

    def test_greater(self):
        [self.assertEqual(self.capture.greater(i[0]), i[1]) for i in GREATER_PROVIDED_VS_EXPECTED_VALUES]

    def test_invalid_keys(self):
        for i in INVALID_KEY_VALUES:
            self.assertRaises(ValueError, lambda: self.capture.less(i))


if __name__ == '__main__':
    unittest.main()
