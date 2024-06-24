from abc import ABC, abstractmethod

class SubjectService(ABC):
  @abstractmethod
  def get_all(self):
    pass
  
  @abstractmethod
  def get_by_name_and_grade(self, name, grade):
    pass
  
  @abstractmethod
  def update(self, subject, id):
    pass
  
  @abstractmethod
  def insert(self, subject):
    pass
  
  @abstractmethod
  def delete(self, id):
    pass