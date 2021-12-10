class TriangleChecker:
    
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_triangle(self):
        if isinstance (self.a, str) or isinstance (self.b, str) or isinstance (self.c, str):
            return 'Нужно вводить только числа'
        
        elif self.a<0 or self.b<0 or self.c<0:
            return 'Нужно вводить только положительные числа'
            
        elif self.a + self.b <= self.c or self.b + self.c <= self.a or self.a + self.c <= self.b:
            return 'Жаль, но из этого треугольника не выйдет'
        
        else:
            return 'Ура можно построить треугольник!'
            
            
triangle = TriangleChecker(-3,4,5)
print(triangle.is_triangle())