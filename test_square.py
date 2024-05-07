from unittest import TestCase
from unittest import main

from square import Square

class TestSquare(TestCase):
  def test_init_raises_type_error(self):
    with self.assertRaises(TypeError):
      square = Square("10")

  def test_init_raises_value_error(self):
    with self.assertRaises(ValueError):
      square = Square(-10)

  def test_area(self):
    square = Square(10)
    area = square.area()
    self.assertEqual(area, 100)
