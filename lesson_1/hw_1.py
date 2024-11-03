class Person:
   # constructor
   def __init__(self, full_name, age, is_married=False):
      self.full_name = full_name
      self.age = age
      self.is_married = is_married
      
   # method
   def introduce_myself(self):
      # return or
      print(f"Name: {self.full_name}\nAge: {self.age}\nMarital status: {self.is_married}")
      
class Student(Person):
      def __init__(self, full_name, age, marks, is_married=False):
         self.full_name = full_name
         self.age = age
         self.marks = marks
         self.is_married = is_married
         
      def arithmetic_mean_estimate(self):
         arithmetic_mean = 0
         for value in self.marks.values():
            arithmetic_mean += value
         return arithmetic_mean / len(self.marks)
      
class Teacher(Person):
   base_salary = 25000 # атрибут уровня класса
   
   def __init__(self, full_name, age, experience, is_married=False):
      self.full_name = full_name
      self.age = age
      self.experience = experience
      self.is_married = is_married
  
   def count_salary(self):
      salary = Teacher.base_salary
      if self.experience > 3:
         extra_years = self.experience - 3
         salary += salary * 0.05 * extra_years
      return salary



teacher_1 = Teacher('Ваня', 25, 5, True)
teacher_1.introduce_myself()
print(teacher_1.count_salary())


def create_students():
    students = []
    
    student1 = Student("Александр Петров", 16, {"math": 5, "russian": 4, "history": 3})
    student2 = Student("Мария Иванова", 17, {"math": 4, "russian": 5, "history": 4})
    student3 = Student("Иван Сидоров", 15, {"math": 3, "russian": 4, "history": 5})
    
    students.extend([student1, student2, student3])
    return students

students_list = create_students()

for student in students_list:
    student.introduce_myself()
    print(f"Marks: {student.marks}")
    average_mark = student.arithmetic_mean_estimate()
    print(f"Average Mark: {average_mark:.2f}\n")