import unittest
from zd2 import TriangleChecker

class TestTriangle(unittest.TestCase):
   
   
    def test_negative_num(self):
        
        triangle = TriangleChecker(-3,4,5)
        triangle_answer=triangle.is_triangle()
    
        self.assertEqual(triangle_answer,'Нужно вводить только положительные числа')
    
    def test_error_num(self):
        
        triangle = TriangleChecker(1,3,10)
        triangle_answer=triangle.is_triangle()
        self.assertEqual(triangle_answer,'Жаль, но из этого треугольника не выйдет')
    def test_true_num(self):
        
        triangle = TriangleChecker(3,4,5)
        triangle_answer=triangle.is_triangle()
        self.assertEqual(triangle_answer,'Ура можно построить треугольник!')
    def test_invalid_num(self):
        
        triangle = TriangleChecker(3,'asd',5)
        triangle_answer=triangle.is_triangle()
        self.assertEqual(triangle_answer,'Нужно вводить только числа')
    