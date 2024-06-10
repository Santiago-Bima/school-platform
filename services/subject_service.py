from abc import ABC, abstractclassmethod

class SubjectService(ABC):
  @abstractclassmethod
  def get_all(self):
    pass