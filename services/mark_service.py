from abc import ABC, abstractclassmethod

class MarkService(ABC):
  @abstractclassmethod
  def get_by_subscription(self, id_subscription):
    pass
  
  @abstractclassmethod
  def insert(self, mark):
    pass