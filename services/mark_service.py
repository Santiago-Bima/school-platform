from abc import ABC, abstractmethod

class MarkService(ABC):
  @abstractmethod
  def get_by_subscription(self, id_subscription):
    pass
  
  @abstractmethod
  def insert(self, mark):
    pass
  
  @abstractmethod
  def update(self, mark, id_mark):
    pass
  
  @abstractmethod
  def delete(self, id_mark):
    pass