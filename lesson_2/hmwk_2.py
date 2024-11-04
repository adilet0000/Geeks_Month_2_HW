class Figure:
   unit = 'cm'

   def __init__(self):
      pass
   
   def calculate_area(self):
      pass

   def info(self):
      pass
   
class Square(Figure):
   def __init__(self, side_length):
      super().__init__
      self.__side_length = side_length
      
   def calculate_area(self):
      return self.__side_length ** 2
   
   def info(self):
      return f"Square side length: {self.__side_length}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}^2."
   
      
class Rectangle(Figure):
   def __init__(self, length, width):
      super().__init__
      self.__length = length
      self.__width = width
      
   def calculate_area(self):
      return self.__length * self.__width
      
   def info(self):
      return f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit},  area: {self.calculate_area()}{Figure.unit}^2."
   
square_1 = Square(25)
# print(square_1.info())
square_2 = Square(5)

rectangle_1 = Rectangle(15, 5)
rectangle_2 = Rectangle(10, 3)
rectangle_3 = Rectangle(25, 15)
# print(rectangle_3.info())

figures_list = [square_1, square_2, rectangle_1, rectangle_2, rectangle_3]

for figure in figures_list:
   print(figure.info())
