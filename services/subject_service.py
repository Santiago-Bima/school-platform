from abc import ABC, abstractclassmethod

class SubjectService(ABC):
  @abstractclassmethod
  def get_all(self):
    pass
  
  @abstractclassmethod
  def get_by_name_and_grade(self, name, grade):
    pass
  
  @abstractclassmethod
  def update(self, subject, id):
    pass
  
  @abstractclassmethod
  def insert(self, subject):
    pass