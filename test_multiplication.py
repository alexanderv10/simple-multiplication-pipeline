import unittest
from multiplication import multiply

class TestMultiplication(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)  # Prueba con números positivos

    def test_negative_numbers(self):
        self.assertEqual(multiply(-3, -4), 12)  # Prueba con números negativos

    def test_mixed_sign_numbers(self):
        self.assertEqual(multiply(-3, 4), -12)  # Prueba con signos mezclados

    def test_zero(self):
        self.assertEqual(multiply(0, 5), 0)  # Prueba con cero

if __name__ == "__main__":
    unittest.main()