import unittest
from math import pi
from area_of_circle import area_of_circle  

class TestCircleArea(unittest.TestCase):
    def test_circle_area(self):
        self.assertEqual(area_of_circle(5), pi * 5**2)
        self.assertEqual(area_of_circle(0), 0)
        self.assertEqual(area_of_circle(10), pi * 10**2)
        with self.assertRaises(ValueError):
            area_of_circle(-5)

if __name__ == "__main__":
    unittest.main()
