class Rectangle:
    def __init__(self,l,w):
        self.a = l
        self.b = w
    def area(self):
        c = self.a*self.b
        return c

i = Rectangle(5,10)
print(i.area())