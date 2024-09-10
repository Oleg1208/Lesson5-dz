import unittest
import math

class TestPythonFunctions(unittest.TestCase):

    def test_filter(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(list(filter(lambda x: x > 3, numbers)), [4, 5])
        self.assertEqual(list(filter(lambda x: x % 2 == 0, numbers)), [2, 4])

    def test_map(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(list(map(lambda x: x * 2, numbers)), [2, 4, 6, 8, 10])
        self.assertEqual(list(map(lambda x: str(x), numbers)), ['1', '2', '3', '4', '5'])

    def test_sorted(self):
        numbers = [5, 2, 8, 1, 4]
        self.assertEqual(sorted(numbers), [1, 2, 4, 5, 8])
        self.assertEqual(sorted(numbers, reverse=True), [8, 5, 4, 2, 1])

    def test_math_pi(self):
        self.assertAlmostEqual(math.pi, 3.141592653589793, places=10)  # Сравнение с точностью до 10 знаков после запятой

    def test_math_sqrt(self):
        self.assertEqual(math.sqrt(9), 3)
        self.assertEqual(math.sqrt(16), 4)

    def test_math_pow(self):
        self.assertEqual(math.pow(2, 3), 8)
        self.assertEqual(math.pow(5, 2), 25)

    def test_math_hypot(self):
        self.assertEqual(math.hypot(3, 4), 5)
        self.assertAlmostEqual(math.hypot(1, 1), 1.4142135623730951, places=10)

if __name__ == '__main__':
    unittest.main()