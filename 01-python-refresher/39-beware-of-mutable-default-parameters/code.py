from typing import List

class Student:
  # def __init__(self, name: str, grades: List[int] = []): # WARNING
  #   self.name = name
  #   self.grades = grades
  def __init__(self, name: str, grades: List[int] = None): # WARNING
    self.name = name
    self.grades = grades or []

  def take_exam(self, result: int):
    self.grades.append(result)

bob = Student("Bob")
rodrigo = Student("Rodrigo")
bob.take_exam(99)
print(bob.grades)
print(rodrigo.grades)