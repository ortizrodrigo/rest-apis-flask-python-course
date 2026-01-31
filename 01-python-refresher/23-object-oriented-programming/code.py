class Student:
  def __init__(self, name):
    self.name = name
    self.grades = (1, 2, 3, 4, 5)

  def average(self):
    return sum(self.grades) / len(self.grades)
  
student = Student("Rodrigo")
print(student.name)
print(student.average())
print(Student.average(student))