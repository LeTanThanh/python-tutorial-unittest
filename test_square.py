from unittest import TestCase
from unittest import main

from square import Square

class TestSquare(TestCase):
  def test_area(self):
    square = Square(10)
    area = square.area()
    self.assertEqual(area, 100)
