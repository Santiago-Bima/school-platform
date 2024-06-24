from abc import ABC, abstractmethod

class SubscriptionService(ABC):
  @abstractmethod
  def get_by_user(self, username):
    pass

  @abstractmethod
  def subscribe(self, subscription):
    pass
  
  @abstractmethod
  def desubscribe(self, id_subscription):
    pass