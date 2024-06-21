from school_platform.services.implementations.subscription_repository_impl import SubscriptionServiceImpl

class SubscriptionController:
  def __init__(self):
    self._service = SubscriptionServiceImpl()
    
  def get_all(self, username):
    subscriptions = self._service.get_by_user(username)
    
    if not subscriptions:
      pass
    
    for i in subscriptions:
      print(i.__str__())
      print()