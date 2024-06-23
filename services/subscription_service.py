from abc import ABC, abstractclassmethod

class SubscriptionService(ABC):
  def get_by_user(self, username):
    pass

  def subscribe(self, subscription):
    pass
  
  def desubscribe(self, id_subscription):
    pass